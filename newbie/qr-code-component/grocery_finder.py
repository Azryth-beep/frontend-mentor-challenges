import requests
import json
from geopy.distance import geodesic
import time

class GroceryStoreFinder:
    def __init__(self):
        self.overpass_url = "http://overpass-api.de/api/interpreter"
        # Velocidad promedio caminando: 5 km/h = 83.33 m/min
        self.walking_speed_mpm = 83.33
    
    def build_overpass_query(self, lat, lng, radius_meters=500):
        """
        Construye la query de Overpass para buscar tiendas de comestibles
        """
        query = f"""
        [out:json][timeout:25];
        (
          node["shop"="supermarket"](around:{radius_meters},{lat},{lng});
          way["shop"="supermarket"](around:{radius_meters},{lat},{lng});
          relation["shop"="supermarket"](around:{radius_meters},{lat},{lng});
          
          node["shop"="convenience"](around:{radius_meters},{lat},{lng});
          way["shop"="convenience"](around:{radius_meters},{lat},{lng});
          
          node["shop"="grocery"](around:{radius_meters},{lat},{lng});
          way["shop"="grocery"](around:{radius_meters},{lat},{lng});
          
          node["amenity"="marketplace"](around:{radius_meters},{lat},{lng});
          way["amenity"="marketplace"](around:{radius_meters},{lat},{lng});
        );
        out center meta;
        """
        return query
    
    def query_overpass(self, query):
        """
        Ejecuta la query contra Overpass API
        """
        try:
            response = requests.get(
                self.overpass_url, 
                params={'data': query},
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error en la consulta: {e}")
            return None
    
    def calculate_walking_time(self, origin_lat, origin_lng, dest_lat, dest_lng):
        """
        Calcula el tiempo estimado caminando usando distancia euclidiana
        """
        distance_km = geodesic((origin_lat, origin_lng), (dest_lat, dest_lng)).kilometers
        distance_meters = distance_km * 1000
        walking_time_minutes = distance_meters / self.walking_speed_mpm
        return walking_time_minutes
    
    def process_results(self, raw_data, origin_lat, origin_lng, max_minutes=5):
        """
        Procesa los resultados de Overpass y filtra por tiempo de caminata
        """
        if not raw_data or 'elements' not in raw_data:
            return []
        
        processed_stores = []
        
        for element in raw_data['elements']:
            # Extraer coordenadas
            if element['type'] == 'node':
                lat, lng = element['lat'], element['lon']
            elif 'center' in element:
                lat, lng = element['center']['lat'], element['center']['lon']
            else:
                continue
            
            # Extraer información de la tienda
            tags = element.get('tags', {})
            
            # Calcular tiempo de caminata
            walking_time = self.calculate_walking_time(origin_lat, origin_lng, lat, lng)
            
            # Filtrar por tiempo máximo
            if walking_time <= max_minutes:
                store_info = {
                    'id': element['id'],
                    'type': element['type'],
                    'name': tags.get('name', 'Sin nombre'),
                    'shop_type': tags.get('shop', tags.get('amenity', 'unknown')),
                    'brand': tags.get('brand', ''),
                    'address': self.build_address(tags),
                    'coordinates': {
                        'lat': lat,
                        'lng': lng
                    },
                    'walking_time_minutes': round(walking_time, 1),
                    'distance_meters': round(walking_time * self.walking_speed_mpm, 0),
                    'opening_hours': tags.get('opening_hours', ''),
                    'phone': tags.get('phone', ''),
                    'website': tags.get('website', ''),
                    'wheelchair': tags.get('wheelchair', ''),
                    'all_tags': tags  # Para debugging
                }
                processed_stores.append(store_info)
        
        # Ordenar por tiempo de caminata
        processed_stores.sort(key=lambda x: x['walking_time_minutes'])
        return processed_stores
    
    def build_address(self, tags):
        """
        Construye una dirección legible desde los tags
        """
        address_parts = []
        
        if 'addr:housenumber' in tags and 'addr:street' in tags:
            address_parts.append(f"{tags['addr:street']} {tags['addr:housenumber']}")
        elif 'addr:street' in tags:
            address_parts.append(tags['addr:street'])
        
        if 'addr:city' in tags:
            address_parts.append(tags['addr:city'])
        
        if 'addr:postcode' in tags:
            address_parts.append(tags['addr:postcode'])
        
        return ', '.join(address_parts) if address_parts else ''
    
    def find_nearby_stores(self, lat, lng, max_minutes=5):
        """
        Función principal para encontrar tiendas cercanas
        """
        print(f"🔍 Buscando tiendas a máximo {max_minutes} minutos caminando desde ({lat}, {lng})")
        
        # Calcular radio en metros (con un poco de buffer)
        radius_meters = int(max_minutes * self.walking_speed_mpm * 1.2)
        
        # Construir y ejecutar query
        query = self.build_overpass_query(lat, lng, radius_meters)
        print(f"📡 Consultando Overpass API (radio: {radius_meters}m)...")
        
        raw_data = self.query_overpass(query)
        if not raw_data:
            return []
        
        # Procesar resultados
        stores = self.process_results(raw_data, lat, lng, max_minutes)
        
        print(f"✅ Encontradas {len(stores)} tiendas en {max_minutes} minutos caminando")
        return stores


def main():
    # Ejemplo de uso
    finder = GroceryStoreFinder()
    
    # Coordenadas de ejemplo (Times Square, NYC - puedes cambiar por tu ubicación)
    my_lat = 40.7580
    my_lng = -73.9855
    
    # Buscar tiendas a máximo 5 minutos caminando
    stores = finder.find_nearby_stores(my_lat, my_lng, max_minutes=5)
    
    # Mostrar resultados en JSON
    if stores:
        print("\n" + "="*60)
        print("TIENDAS ENCONTRADAS (JSON)")
        print("="*60)
        
        # JSON completo
        result = {
            "search_location": {
                "lat": my_lat,
                "lng": my_lng
            },
            "search_radius_minutes": 5,
            "total_stores_found": len(stores),
            "stores": stores
        }
        
        print(json.dumps(result, indent=2, ensure_ascii=False))
        
        # Resumen legible
        print("\n" + "="*60)
        print("RESUMEN LEGIBLE")
        print("="*60)
        
        for i, store in enumerate(stores, 1):
            print(f"\n{i}. {store['name']} ({store['shop_type']})")
            print(f"   📍 {store['coordinates']['lat']}, {store['coordinates']['lng']}")
            print(f"   🚶 {store['walking_time_minutes']} minutos ({store['distance_meters']}m)")
            if store['address']:
                print(f"   📮 {store['address']}")
            if store['brand']:
                print(f"   🏪 {store['brand']}")
            if store['opening_hours']:
                print(f"   🕒 {store['opening_hours']}")
    else:
        print("❌ No se encontraron tiendas en el radio especificado")


if __name__ == "__main__":
    main()
# Frontend Mentor - Blog preview card solution

This is a solution to the [Blog preview card challenge on Frontend Mentor](https://www.frontendmentor.io/challenges/blog-preview-card-EXPO1Fyvf). Frontend Mentor challenges help you improve your coding skills by building realistic projects.

## Table of contents

- [Frontend Mentor - Blog preview card solution](#frontend-mentor---blog-preview-card-solution)
  - [Table of contents](#table-of-contents)
  - [Overview](#overview)
    - [Screenshot](#screenshot)
    - [Links](#links)
  - [My process](#my-process)
    - [Built with](#built-with)
    - [What I learned](#what-i-learned)
    - [Continued development](#continued-development)
    - [Useful resources](#useful-resources)
  - [Author](#author)

## Overview

### Screenshot

![](./results/blog-preview-card.png)

**Active States:**
![](./results/blog-preview-card_active.png)

### Links

- Live Site URL: [Add your live site URL here]
- Solution URL: [Add your Frontend Mentor solution URL here]

**Note**: This project can be hosted on platforms like Netlify, Vercel, or GitHub Pages for live preview.

## My process

### Built with

- Semantic HTML5 markup with proper accessibility attributes
- CSS custom properties (CSS variables) for maintainable design system
- CSS Flexbox for layout and centering
- Mobile-first responsive design workflow
- Local Figtree font files with variable font support
- Modern CSS practices including HSL colors and smooth transitions
- Hover states and focus accessibility

### What I learned

This project reinforced several important concepts for me:

**CSS Custom Properties & Design Systems**: I implemented a comprehensive design system using CSS variables for colors, typography, and spacing. This made the code much more maintainable and consistent.

```css
:root {
  --color-yellow: hsl(47, 88%, 63%);
  --color-white: hsl(0, 0%, 100%);
  --color-gray-500: hsl(0, 0%, 42%);
  --color-gray-950: hsl(0, 0%, 7%);
  --font-weight-medium: 500;
  --font-weight-extrabold: 800;
}
```

**Local Font Implementation**: I learned how to properly implement local font files using @font-face declarations, including variable fonts for better performance and flexibility.

```css
@font-face {
  font-family: 'Figtree';
  src: url('../assets/fonts/Figtree-VariableFont_wght.ttf') format('truetype-variations');
  font-weight: 300 900;
  font-style: normal;
}
```

**Mobile-First Responsive Design**: Using a mobile-first approach with CSS custom properties made it easy to create a design that works seamlessly across all device sizes, from 375px mobile to 1440px desktop.

**Interactive States**: I implemented hover effects and focus states that enhance user experience while maintaining accessibility standards.

**CSS Layout Techniques**: I practiced using Flexbox for layout management and learned how to create proper spacing and alignment for card-based designs.

### Continued development

Moving forward, I want to focus on:

- **CSS Grid**: While Flexbox worked perfectly for this layout, I want to practice CSS Grid for more complex layouts
- **CSS Animations**: I'd like to explore more advanced animations and micro-interactions
- **CSS-in-JS**: I'm interested in learning styled-components or emotion for larger projects
- **Accessibility Testing**: I want to learn more about automated accessibility testing tools
- **Performance Optimization**: I want to explore font loading strategies and image optimization techniques

### Useful resources

- [CSS Custom Properties Guide](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties) - This helped me understand how to create a proper design system with CSS variables
- [CSS @font-face Rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face) - Essential for implementing local fonts
- [CSS-Tricks Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) - Excellent reference for Flexbox properties and use cases
- [Variable Fonts Guide](https://web.dev/variable-fonts/) - Helped me understand how to implement variable fonts for better performance
- [Frontend Mentor Style Guide](https://www.frontendmentor.io/learn) - Great resource for understanding design requirements and best practices

## Author

- **Your Name** - Frontend Developer
- LinkedIn - [Your LinkedIn Profile]
- GitHub - [Your GitHub Profile]
- Frontend Mentor - [Your Frontend Mentor Profile]

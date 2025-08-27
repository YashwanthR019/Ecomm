# Amazon Clone - Separated Architecture

A modern e-commerce website built with Flask, featuring a clean separation of HTML, CSS, and JavaScript.

## 🚀 Features

- **Product Catalog**: Browse products with images, descriptions, and ratings
- **Search & Filter**: Search by product name, filter by category and brand
- **Shopping Cart**: Add/remove items, view cart total
- **Responsive Design**: Mobile-friendly interface
- **Modern UI**: Beautiful gradients, animations, and hover effects
- **Stock Tracking**: Real-time stock indicators
- **API Endpoints**: RESTful API for future enhancements

## 📁 Project Structure

```
Amazon_Clone/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css     # All CSS styles
│   └── js/
│       └── script.js     # JavaScript functionality
└── README.md             # This file
```

## 🛠️ Architecture Benefits

### HTML (`templates/index.html`)
- Clean, semantic markup
- Jinja2 templating for dynamic content
- Proper separation of structure from presentation

### CSS (`static/css/style.css`)
- Modular, organized styles
- Responsive design with media queries
- Modern CSS features (Grid, Flexbox, Gradients)
- Hover effects and animations

### JavaScript (`static/js/script.js`)
- Enhanced user interactions
- Form validation and confirmation dialogs
- Loading states and animations
- Accessibility improvements
- Future-ready for AJAX functionality

## 🚀 Getting Started

### Local Development

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python app.py
   ```

3. **Access the Website**:
   - Open your browser and go to: `http://localhost:8080`
   - Or visit: `http://127.0.0.1:8080`

### Production Deployment

For production deployment to PythonAnywhere, see [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

## 🔧 API Endpoints

- `GET /api/product/<id>` - Get product details
- `GET /api/cart` - Get cart summary

## 📱 Features

### Product Features
- Product grid with hover effects
- Stock level indicators
- Rating display with stars
- Add to cart functionality
- Product images with zoom effect

### Search & Filter
- Real-time search by product name, description, or brand
- Category filtering (Electronics, Shoes)
- Brand filtering (Apple, Sony, Nike, Samsung, Adidas)
- Sorting options (Price, Rating, Name)

### Shopping Cart
- Add items to cart
- Remove individual items
- Clear entire cart
- View cart total
- Checkout simulation

### User Experience
- Responsive design for all devices
- Smooth animations and transitions
- Loading states for better feedback
- Keyboard navigation support
- Accessibility features (ARIA labels, focus indicators)

## 🎨 Design Features

- **Color Scheme**: Amazon-inspired orange and dark blue
- **Typography**: Clean, readable fonts
- **Layout**: CSS Grid for product display
- **Animations**: Smooth hover effects and transitions
- **Mobile-First**: Responsive design that works on all devices

## 🔮 Future Enhancements

The separated architecture makes it easy to add:
- User authentication
- Payment processing
- Product reviews
- Wishlist functionality
- Advanced search filters
- AJAX cart updates
- Product recommendations

## 📝 Development Notes

- **Flask**: Uses Flask's template system for server-side rendering
- **Static Files**: CSS and JS are served from the `static/` directory
- **Session Management**: Shopping cart is stored in Flask sessions
- **Product Data**: Currently uses in-memory data (can be replaced with database)

## 🎯 Best Practices Implemented

- **Separation of Concerns**: HTML, CSS, and JS are completely separated
- **Responsive Design**: Mobile-first approach with CSS Grid and Flexbox
- **Accessibility**: ARIA labels, keyboard navigation, focus indicators
- **Performance**: Optimized images, efficient CSS, minimal JavaScript
- **Maintainability**: Clean, well-organized code structure

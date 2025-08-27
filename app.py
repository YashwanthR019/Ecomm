# Ecomm website - Quick Setup Version
# Save this as app.py and run: python app.py

from flask import Flask, render_template, request, session, redirect, url_for, jsonify

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'

# Adding some sample products
products = [
    {
        'id': 1, 'title': 'iPhone 15 Pro', 'price': 999.99, 'rating': 4.8,
        'image': 'https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=300&h=300&fit=crop',
        'category': 'Electronics', 'description': 'Latest iPhone with Pro camera system',
        'stock': 25, 'brand': 'Apple'
    },
    {
        'id': 2, 'title': 'Sony WH-1000XM4 Headphones', 'price': 349.99, 'rating': 4.6,
        'image': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=300&h=300&fit=crop',
        'category': 'Electronics', 'description': 'Industry-leading noise canceling headphones',
        'stock': 15, 'brand': 'Sony'
    },
    {
        'id': 3, 'title': 'Nike Air Max 270', 'price': 129.99, 'rating': 4.5,
        'image': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=300&h=300&fit=crop',
        'category': 'Shoes', 'description': 'Comfortable running shoes with Max Air unit',
        'stock': 30, 'brand': 'Nike'
    },
    {
        'id': 4, 'title': 'MacBook Air M2', 'price': 1199.99, 'rating': 4.9,
        'image': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=300&h=300&fit=crop',
        'category': 'Electronics', 'description': 'Supercharged by M2 chip',
        'stock': 12, 'brand': 'Apple'
    },
    {
        'id': 5, 'title': 'Samsung Galaxy Watch', 'price': 279.99, 'rating': 4.4,
        'image': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=300&h=300&fit=crop',
        'category': 'Electronics', 'description': 'Advanced smartwatch with health tracking',
        'stock': 20, 'brand': 'Samsung'
    },
    {
        'id': 6, 'title': 'Adidas Ultraboost 22', 'price': 179.99, 'rating': 4.3,
        'image': 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=300&h=300&fit=crop',
        'category': 'Shoes', 'description': 'Energy-returning running shoes',
        'stock': 18, 'brand': 'Adidas'
    }
]

@app.route('/')
def home():
    # Get search and filter parameters
    search_query = request.args.get('search', '').lower()
    category_filter = request.args.get('category', '')
    sort_by = request.args.get('sort', '')
    brand_filter = request.args.get('brand', '')
    
    # Filter products based on search and filters
    filtered_products = products.copy()
    
    # Apply search filter
    if search_query:
        filtered_products = [p for p in filtered_products 
                           if search_query in p['title'].lower() or 
                              search_query in p['description'].lower() or
                              search_query in p['brand'].lower()]
    
    # Apply category filter
    if category_filter:
        filtered_products = [p for p in filtered_products if p['category'] == category_filter]
    
    # Apply brand filter
    if brand_filter:
        filtered_products = [p for p in filtered_products if p['brand'] == brand_filter]
    
    # Apply sorting
    if sort_by == 'price_low':
        filtered_products.sort(key=lambda x: x['price'])
    elif sort_by == 'price_high':
        filtered_products.sort(key=lambda x: x['price'], reverse=True)
    elif sort_by == 'rating':
        filtered_products.sort(key=lambda x: x['rating'], reverse=True)
    elif sort_by == 'name':
        filtered_products.sort(key=lambda x: x['title'])
    
    # Get cart from session
    cart = session.get('cart', [])
    cart_items = []
    total_price = 0
    
    # Count quantity of each item
    cart_counts = {}
    for item_id in cart:
        cart_counts[item_id] = cart_counts.get(item_id, 0) + 1
    
    # Get product details with quantities
    for item_id, quantity in cart_counts.items():
        product = next((p for p in products if p['id'] == item_id), None)
        if product:
            item_data = product.copy()
            item_data['quantity'] = quantity
            item_data['subtotal'] = product['price'] * quantity
            cart_items.append(item_data)
            total_price += item_data['subtotal']
    
    return render_template('index.html', 
                         filtered_products=filtered_products,
                         cart_items=cart_items,
                         cart_count=len(cart),
                         total_price=total_price,
                         request=request)

@app.route('/add-to-cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # Check if product exists
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return redirect(url_for('home'))
    
    # Initialize cart if it doesn't exist
    if 'cart' not in session:
        session['cart'] = []
    
    # Check stock (simple check - in real app you'd check against database)
    cart = session['cart']
    current_quantity = cart.count(product_id)
    
    if current_quantity < product['stock']:
        session['cart'].append(product_id)
        session.modified = True
    
    return redirect(url_for('home'))

@app.route('/remove-from-cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    if 'cart' in session:
        cart = session['cart']
        if product_id in cart:
            cart.remove(product_id)
            session.modified = True
    
    return redirect(url_for('home'))

@app.route('/clear-cart', methods=['POST'])
def clear_cart():
    session['cart'] = []
    session.modified = True
    return redirect(url_for('home'))

# API endpoint for getting product details (for future AJAX functionality)
@app.route('/api/product/<int:product_id>')
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

# API endpoint for cart summary
@app.route('/api/cart')
def get_cart():
    cart = session.get('cart', [])
    cart_counts = {}
    for item_id in cart:
        cart_counts[item_id] = cart_counts.get(item_id, 0) + 1
    
    cart_items = []
    total_price = 0
    
    for item_id, quantity in cart_counts.items():
        product = next((p for p in products if p['id'] == item_id), None)
        if product:
            subtotal = product['price'] * quantity
            cart_items.append({
                'id': product['id'],
                'title': product['title'],
                'price': product['price'],
                'quantity': quantity,
                'subtotal': subtotal
            })
            total_price += subtotal
    
    return jsonify({
        'items': cart_items,
        'total_items': len(cart),
        'total_price': total_price
    })

if __name__ == '__main__':
    print("🚀 Starting Enhanced Amazon Clone...")
    print("✨ New Features:")
    print("   • Search functionality")
    print("   • Category and brand filters")
    print("   • Product sorting")
    print("   • Enhanced UI with animations")
    print("   • Stock tracking")
    print("   • API endpoints")
    print("   • Mobile responsive design")
    print("   • Separated HTML/CSS/JS architecture")
    print("\n📱 Access your store at:")
    print("   http://localhost:8080")
    print("   http://127.0.0.1:8080")
    print("\n🔧 API Endpoints:")
    print("   GET /api/product/<id> - Get product details")
    print("   GET /api/cart - Get cart summary")
    print("\n📁 File Structure:")
    print("   templates/index.html - Main HTML template")
    print("   static/css/style.css - All styles")
    print("   static/js/script.js - Interactive features")
    
    # Development server
    app.run(debug=True, host='0.0.0.0', port=8080)
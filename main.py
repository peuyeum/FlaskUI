from flask import render_template
from flask import Flask,abort,Response
app = Flask(__name__)

PRODUCTS = {
    'iphone': {
        'name': 'iPhone 5S',
        'category': 'Phones',
        'price': 699,
    },
    'galaxy': {
        'name': 'Samsung Galaxy 5',
        'category': 'Phones',
        'price': 649,
    },
    'ipad-air': {
        'name': 'iPad Air',
        'category': 'Tablets',
        'price': 649,
    },
    'ipad-mini': {
        'name': 'iPad Mini',
        'category': 'Tablets',
        'price': 549
    }
}

@app.route("/")
def home():
	name="ganteng"
	return render_template('home.html', products=PRODUCTS, SignIn=True, SignUp=True)
	
@app.route('/product/<key>')
def product(key):
    product = PRODUCTS.get(key)
    if not product:
        abort(404)
    return render_template('product.html', product=product)

@app.route("/login")
def login():
	name="ganteng"
	return render_template('login.html', name=name)

@app.route("/signup")
def signup():
	name="ganteng"
	return render_template('signup.html', name=name)
	



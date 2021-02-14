from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import ProductForm
from app.models import Product

@app.route('/')
@app.route('/index')
def index():
    db.create_all()
    all_products = Product.query.all()
    return render_template("index.html", products=all_products)

@app.route('/products')
def products():
    all_products = Product.query.all()
    return render_template("products.html", data=all_products)

@app.route('/product/<id>')
def get_product(id):
    product = Product.query.get(id)
    if not product.photo_url:
       product.photo_url = url_for('static', filename='nopicture.jpg')
    return render_template("product_detail.html", product=product)    

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data, description=form.description.data, price=form.price.data, photo_url=form.photo_url.data)
        db.session.add(product)
        db.session.commit()
        flash('Product created successfully!', 'success')
        return redirect(url_for('products'))
    return render_template('add_product.html', title='Add Product', form=form)
import os
import secrets
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

def save_photo(form_photo):
    random_hex = secrets.token_hex(5)
    _, f_ext = os.path.splitext( form_photo.filename)
    photo_filename = random_hex + f_ext
    photo_path = os.path.join(app.root_path, 'static/product_pics', photo_filename)
    form_photo.save(photo_path)

    return photo_filename

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        if form.photo_url.data:
            photo_filename = save_photo(form.photo_url.data)
        product = Product(name=form.name.data, description=form.description.data,
                          price=form.price.data, photo_url=url_for('static', filename='product_pics/' + photo_filename))
        db.session.add(product)
        db.session.commit()
        flash('Product created successfully!', 'success')
        return redirect(url_for('products'))
    return render_template('add_product.html', title='Add Product', form=form)
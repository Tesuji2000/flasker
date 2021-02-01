from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
# def index():
#     return "<h1>Hello World ! </h1>"
# localhost:5000/
# filters
# safe
# upper
# lower
# capitalize
# title
# trim
# striptags
def index():
    first_name = 'Dave'
    crypto_link = 'https://nomics.com/'
    stuff = "This is <strong>Bold</strong> text."
    favorite_pizza = ["Pepperoni", "Cheese", "Sausage"]
    a_list = [12, 'abc', [1, 2, 3], 'tomorrow is monday']
    return render_template('index.html',
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza,
                           crypto_link=crypto_link,
                           a_list=a_list
                           )

# localhost:5000/user/Dave
@app.route('/user/<name>')
def user(name):
    # return "<h1>Hello {} </h1>".format(name)
    # return f"<h1>Hello {name} </h1>"
    return render_template('user.html', user_name=name)

# Create custom error pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

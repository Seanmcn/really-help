from flask import Flask, render_template
from flask.ext.bcrypt import Bcrypt
from database import db_session
from models import *

app = Flask(__name__)
app.config['SERVER_NAME'] = '127.0.0.1:5000'
bcrypt = Bcrypt(app)


@app.route('/')
def home():
    data = dict()
    data['categories'] = db_session.query(Categories).order_by(Categories.name).all()
    return render_template('home.html', data=data)


# Todo: Thinking of it this is pointless, category should just link to search page with facet applied.
@app.route('/category/<slug>')
def category(slug):
    data = dict()
    data['slug'] = slug

    # Get Categories
    data['categories'] = db_session.query(Categories).order_by(Categories.name).all()

    data['charities'] = []

    a_charity = dict()
    a_charity['id'] = 'one_drop'
    a_charity['name'] = 'One Drop'
    a_charity['short_description'] = 'One drop does thing with water for people who need it! They\'re great'
    a_charity['rating'] = 5
    data['charities'].append(a_charity)

    a_charity = dict()
    a_charity['id'] = 'bad_charity'
    a_charity['name'] = 'Bad Charity'
    a_charity['short_description'] = 'This charity doen\'t spend a lot of their money on their charity'
    a_charity['rating'] = 2
    data['charities'].append(a_charity)
    # Get Charities

    return render_template('category.html', data=data)


@app.route('/search')
def search():
    data = dict()
    return render_template('category.html', data=data)


@app.route('/charity/<int:id>')
def charity(id):
    # Get Single Charity
    data = []
    return render_template('charity.html', data=data)


@app.route('/register')
def register():
    # pw_hash = bcrypt.generate_password_hash(password)
    return render_template('user/register.html')


# Todo: Post Register?


@app.route('/login')
def login():
    # bcrypt.check_password_hash(pw_hash, 'hunter2')  # returns True
    return render_template('user/login.html')


# Todo: Post login?

@app.route('/admin')
def admin():
    # Probably setting data?
    return render_template('admin/dashboard.html')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()

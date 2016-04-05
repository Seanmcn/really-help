from flask import Flask, render_template
from flask.ext.bcrypt import Bcrypt
from database import db_session
from models import *

app = Flask(__name__)
bcrypt = Bcrypt(app)


@app.route('/')
def home():
    # Get Categories
    return render_template('home.html')


@app.route('/category/<category>')
def category(category):
    # Get Charities
    data = []
    return render_template('category.html', dara=data)


@app.route('/charity/<int:id>')
def charity(id):
    # Get Single Charity
    data = []
    return render_template('charity.html', dara=data)


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

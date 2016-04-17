from flask import Flask, render_template, redirect, url_for
from database import db_session
from flask.ext.bcrypt import Bcrypt
from models import *
from forms import LoginForm
from flask_wtf.csrf import CsrfProtect

import flask.ext.login as flask_login

# APP CONFIG
app = Flask(__name__)
app.config['SERVER_NAME'] = '127.0.0.1:5000'
app.secret_key = 'SomeSECR3TSt5ing'  # Todo Sean: Update before push to PROD.

csrf = CsrfProtect(app)
# csrf.init_app(app)

# LOGIN CONFIG
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)


@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve
    """
    return User.query.get(user_id)


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
    return render_template('user/register.html')


@app.route('/login', methods=("GET", "POST"))
def login():
    """For GET requests, display the login form. For POSTS, login the current user
       by processing the form."""
    form = LoginForm()
    print('Im the form')

    if form.validate_on_submit():
        print('here!')
        user = User.query.get(form.email.data)
        if user:
            print('is user')
            if bcrypt.check_password_hash(user.password, form.password.data):
                print('authenticated')
                user.authenticated = True
                db_session.add(user)
                db_session.commit()
                flask_login.login_user(user, remember=True)
                return redirect(url_for("admin"))
    print(form.errors)
    print('else hit')
    return render_template('user/login.html', form=form)


@flask_login.login_required
@app.route('/logout', methods=["GET"])
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    db_session.add(user)
    db_session.commit()
    flask_login.logout_user()
    return render_template("logout.html")


@flask_login.login_required
@app.route('/admin')
def admin():
    # Probably setting data?
    return render_template('admin/dashboard.html')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()

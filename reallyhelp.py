from flask import Flask
from flask.ext.bcrypt import Bcrypt
from database import db_session
from models import User

app = Flask(__name__)
bcrypt = Bcrypt(app)


@app.route('/')
def hello_world():
    user = User.query.filter(User.name == 'admin').first().name
    return 'Hello ' + str(user) + '!'


@app.route('/register')
def register():
    # pw_hash = bcrypt.generate_password_hash(password)
    return 'Register'


@app.route('/login')
def login():
    # bcrypt.check_password_hash(pw_hash, 'hunter2')  # returns True
    return 'Login'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()

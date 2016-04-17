#!/usr/bin/env python
"""Create a new admin user able to view the /reports endpoint."""
from getpass import getpass
from reallyhelp import app
from database import db_session
from flask.ext.bcrypt import Bcrypt
from models import User

import sys


def main():
    """Main entry point for script."""
    with app.app_context():
        bcrypt = Bcrypt(app)
        if User.query.all():
            print('A user already exists! Create another? (y/n):'),
            create = input()
            if create == 'n':
                return

        print('Enter email address: '),
        email = input()
        password = getpass()
        assert password == getpass('Password (again):')

        user = User(email=email, password=bcrypt.generate_password_hash(password))
        db_session.add(user)
        db_session.commit()
        print('User added.')


if __name__ == '__main__':
    sys.exit(main())

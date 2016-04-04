from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    pw_hash = Column(String(60)) # Todo: This only being 60 seems wrong, test.
    email = Column(String(120), unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    role = Column(Integer())

    def __init__(self, username, pw_hash=None, email=None, first_name=None, last_name=None, role=None):
        self.username = username
        self.pw_hash = pw_hash
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

    def __repr__(self):
        return '<User %r>' % self.name

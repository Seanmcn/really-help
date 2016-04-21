from sqlalchemy import Table, Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship

from database import Base

charities_categories = Table('charities_categories', Base.metadata,
                             Column('charity_id', Integer, ForeignKey('charities.id')),
                             Column('category_id', Integer, ForeignKey('categories.id'))
                             )

charities_tags = Table('charities_tags', Base.metadata,
                       Column('charity_id', Integer, ForeignKey('charities.id')),
                       Column('tag_id', Integer, ForeignKey('tags.id'))
                       )


class Charities(Base):
    __tablename__ = 'charities'
    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    description = Column(Text)
    website = Column(String(300))  # Todo: probably not long enough
    donate_link = Column(String(300))  # Todo: probably not long enough
    rating = Column(Integer)
    categories = relationship("Categories", secondary=charities_categories)
    tags = relationship("Tags", secondary=charities_tags)
    records = relationship("Records")
    achievements = relationship("Achievements")

    def __repr__(self):
        return '<Charities %r>' % self.name


class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    slug = Column(String(30), unique=True)
    icon_class = Column(String(30))

    def __init__(self, slug, name=None):
        self.slug = slug
        self.name = name

    def __repr__(self):
        return '<Categories %r>' % self.name


class Tags(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    slug = Column(String(30), unique=True)

    def __init__(self, slug, name=None):
        self.slug = slug
        self.name = name

    def __repr__(self):
        return '<Tags %r>' % self.name


class Records(Base):
    # Todo: figure out fields
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    charity_id = Column(Integer, ForeignKey('charities.id'))


class Achievements(Base):
    # Todo: figure out fields
    __tablename__ = 'achievements'
    id = Column(Integer, primary_key=True)
    charity_id = Column(Integer, ForeignKey('charities.id'))


#
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     username = Column(String(50), unique=True)
#     pw_hash = Column(String(60))  # Todo: This only being 60 seems wrong, test.
#     email = Column(String(120), unique=True)
#     first_name = Column(String(50))
#     last_name = Column(String(50))
#     role_id = Column(Integer, ForeignKey('users_roles.id'))
#     role = relationship("UserRoles")
#
#     def __init__(self, username, pw_hash=None, email=None, first_name=None, last_name=None, role=None):
#         self.username = username
#         self.pw_hash = pw_hash
#         self.email = email
#         self.first_name = first_name
#         self.last_name = last_name
#         self.role = role
#
#     def __repr__(self):
#         return '<User %r>' % self.name

class User(Base):
    """An admin user capable of viewing reports.

    :param str email: email address of user
    :param str password: encrypted password for the user

    """
    __tablename__ = 'users'

    email = Column(String(120), primary_key=True)
    password = Column(String(60))
    authenticated = Column(Boolean, default=False)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
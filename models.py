from sqlalchemy import Column, Integer, String
from database import Base


class Charities(Base):
    __tablename__ = 'charities'
    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    description = Column()  # Todo: Find out text type
    website = Column(String(300))  # Todo: probably not long enough
    donate_link = Column(String(300))  # Todo: probably not long enough

    # Todo: to-many -> Categories
    # Todo: to-many -> Records
    # Todo: to-many -> Tags

    def __repr__(self):
        return '<Charities %r>' % self.name


class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    slug = Column(String(30), unique=True)

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
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)


class Achievements(Base):
    __tablename__ = 'achivements'
    id = Column(Integer, primary_key=True)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    pw_hash = Column(String(60))  # Todo: This only being 60 seems wrong, test.
    email = Column(String(120), unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    role = Column(Integer())  # Todo: Map to single role

    def __init__(self, username, pw_hash=None, email=None, first_name=None, last_name=None, role=None):
        self.username = username
        self.pw_hash = pw_hash
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

    def __repr__(self):
        return '<User %r>' % self.name


class UserRoles(Base):
    __tablename__ = 'users_roles'
    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, unique=True)
    name = Column(String(30))

    def __init__(self, role_id, name):
        self.role_id = role_id
        self.name = name


class RegisterTokens(Base):
    __tablename__ = 'users_tokens'
    id = Column(Integer, primary_key=True)
    token = Column(String(150), unique=True)
    role_id = Column(Integer())  # Todo: map to single
    active = Column()  # Find out boolean type

    def __init__(self, token, role):
        self.token = token  # Todo: auto generate
        self.role = role

        # Todo: Active mode.

import sqlalchemy as sa
import sqlalchemy.orm as so
from models import User, Post, Comment, Base

sqlite_engine = sa.create_engine('sqlite:///social_media.db', echo=True)

# Create a session
session = so.Session(bind=sqlite_engine)

# Create examples of Users

uname = input('Enter your username: ')
uage = input('Enter your age: ')
if uage == '':
    uage = None
else:
    uage = int(uage)
ugender = input('Enter your gender: ')
if ugender == '':
    ugender = None
unationality = input('Enter your nationality: ')
if unationality == '':
    unationality = None

users = [User(name=uname, age=uage, gender=ugender, nationality=unationality),
         ]

session.add_all(users)
session.commit()
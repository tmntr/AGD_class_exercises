import sqlalchemy as sa
import sqlalchemy.orm as so
from models import User, Post, Comment, Base

engine = sa.create_engine('sqlite:///social_media.db', echo=True)

# Create examples of Users

def add_user(engine,uname,uage = None,ugender = None,unationality = None):
    engine = sa.create_engine('sqlite:///social_media.db', echo=True)
    # Create a session
    session = so.Session(bind=engine)
    users = [User(name=uname, age=uage, gender=ugender, nationality=unationality),
             ]
    session.add_all(users)
    session.commit()

def create_user(engine):

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
    add_user(engine,uname, uage, ugender, unationality)


'''
users = [User(name="Alice", age=30, gender="Female", nationality="Canadian"),
             User(name="Bob", age=25, gender="Male", nationality="American"),
             User(name="Charlie", age=28, gender="Male", nationality="British"),
             User(name="Diana", age=22, gender="Female", nationality="Australian"),]
'''

create_user()

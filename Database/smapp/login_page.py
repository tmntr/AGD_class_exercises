import sqlalchemy as sa
import sqlalchemy.orm as so
from models import User, Post, Comment, Base
from user_management import create_user, add_user

engine =

accepted = False
while not accepted:
    uname = input("Username: ")
    search =
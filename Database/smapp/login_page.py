import sqlalchemy as sa
import sqlalchemy.orm as so
from models import User, Post, Comment, Base
from user_management import create_user, user_exists, get_userid
from post_management import view_posts_by_user, make_post

class stage:
    def __init__(self,engine):
        self._currentstage = 'login'
        self._user = ''
        self.engine = engine

    @property
    def currentstage(self):
        return self._currentstage
    @currentstage.setter
    def currentstage(self, value):
        self._currentstage = value

    @property
    def user(self):
        return self._user
    @user.setter
    def user(self, value):
        self._user = value

    def login(self):
        accepted = False

        while not accepted:
            uname = input("Username: ")
            search = user_exists(self.engine, uname)
            if search:
                accepted = True
                self.user = uname
                self.currentstage = 'homepage'
            else:
                print("No such user. Would you like to create a new user?")
                if input('y/n: ').lower() == 'y':
                    create_user(self.engine)
                    accepted = True
                    self.user = uname
                    self.currentstage = 'homepage'

    def homepage(self):
        options = ['Look at posts','Make a post','Return to login page']
        for i in range(len(options)):
            print(f"{i+1}: {options[i]}")
        action = input("Choose an option: ")
        if action == '1':
            self.currentstage = 'posts'
        elif action == '2':
            self.currentstage = 'post_making'
        elif action == '3':
            self.currentstage = 'login'

    def posts(self):
        options = ['View a specific user\'s posts', 'View posts by recency', 'View posts by likes', 'Comment on a post by ID', 'Like a post by ID']
        for i in range(len(options)):
            print(f"{i + 1}: {options[i]}")
        action = input("Choose an option: ")
        if action == '1':
            username = input("Whose posts would you like to view: ")
            posts = view_posts_by_user(self.engine, username)
            for item in posts:
                print(item.title)
                print('='*len(item.title))
                print(item.content)

    def post_making(self):
        title = input("Enter a title: ")
        content = input("Enter a content: ")
        currentuserid = get_userid(self.engine,self.user)

        make_post(self.engine,title,content,currentuserid)

        action = input("Would you like to make another post? y/n: ")

        if action != 'y':
            self.currentstage = 'homepage'



    def run(self):
        stages = {'login':self.login, 'homepage':self.homepage,'posts':self.posts, 'post_making':self.post_making}
        nextmove = stages[self.currentstage]
        nextmove()


engine = sa.create_engine('sqlite:///social_media.db', echo=False)

stage = stage(engine)
while True:
    stage.run()
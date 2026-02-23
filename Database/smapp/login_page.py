import sqlalchemy as sa
import sqlalchemy.orm as so
from models import User, Post, Comment, Base
from user_management import *
from post_management import *

def display_post(item):
    print('\n')
    banner = f"{item.id}:\'{item.title}\', by {item.user.name}"
    print(banner)
    print('=' * max([len(banner),len(item.description)]))
    print(item.description)
    print(f"{item.number_of_likes()} Likes")
    print('\n')

def display_comment(item):
    print('\n')
    banner = f"{item.user.name}'s comment on post {item.post_id}: \'{item.post.title}\', by {item.post.user.name}"
    print(banner)
    print('=' * max([len(banner),len(item.comment)]))
    print(item.comment)
    print('\n')

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
        options = ['View a specific user\'s posts', 'View posts by recency', 'View posts by likes', 'Comment on a post by ID', 'Like a post by ID','View all the comments on a particular post','Make a post','Exit to homepage']
        for i in range(len(options)):
            print(f"{i + 1}: {options[i]}")
        action = input("Choose an option: ")
        if action == '1':
            username = input("Whose posts would you like to view: ")
            posts = view_posts_by_user(self.engine, username)
            for item in posts:
                display_post(item)
        elif action == '2':
            posts = view_posts_by_recency(self.engine)
            for item in posts:
                display_post(item)
        elif action == '3':
            posts = view_posts_by_likes(self.engine)
            for item in posts:
                display_post(item)
        elif action == '4':
            postid = input("Which post would you like to comment on: ")
            if post_exists(self.engine, postid):
                comment = input("What would you like to say: ")
                make_comment(self.engine, postid, self.user, comment)
            else:
                print("No such post.")
        elif action == '5':
            postid = input("Which post would you like to like: ")
            like_post(self.engine, postid, self.user)
        elif action == '6':
            postid = input("Which post would you like to view the comments of: ")
            if post_exists(self.engine, postid):
                for item in view_comments(self.engine, postid):
                    display_comment(item)
        elif action == '7':
            self.currentstage = 'post_making'
        elif action == '8':
            self.currentstage = 'homepage'

    def post_making(self):
        title = input("Enter a title: ")
        content = input("Enter a content: ")
        currentuserid = get_userid(self.engine,self.user)

        make_post(self.engine,title,content,currentuserid)

        action = input("Would you like to make another post? y/n: ")

        if action != 'y':
            self.currentstage = 'posts'



    def run(self):
        stages = {'login':self.login, 'homepage':self.homepage,'posts':self.posts, 'post_making':self.post_making}
        nextmove = stages[self.currentstage]
        nextmove()


engine = sa.create_engine('sqlite:///social_media.db', echo=False)

stage = stage(engine)
while True:
    stage.run()
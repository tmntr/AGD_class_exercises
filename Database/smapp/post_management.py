import sqlalchemy as sa
import sqlalchemy.orm as so
from models import User, Post, Comment, Base

def view_posts_by_recency(engine):
    session = so.Session(bind=engine)
    qry = (sa.select(Post))
    posts = session.scalars(qry).all()

    return posts

def view_posts_by_user(engine,uname):
    session = so.Session(bind=engine)

    qry = (sa.select(Post).join(User)
           .filter(User.name == uname and Post.user_id == User.id))

    posts = session.scalars(qry).all()

    return posts

def view_posts_by_likes(engine):
    session = so.Session(bind=engine)

    qry = (sa.select(Post).order_by(len(Post.liked_by_users)))

    posts = session.scalars(qry).all()

    return posts

def like_post(engine,postid,user):
    session = so.Session(bind=engine)

    userqry = (sa.select(User).filter(User.name == user))
    theuser = session.scalar(userqry)

    qry = (sa.select(Post).filter(Post.id == postid))

    thepost = session.scalar(qry)

    if thepost and theuser not in thepost.liked_by_users:
        thepost.liked_by_users.append(theuser)

        print(thepost.number_of_likes())
    session.commit()




def make_post(engine,title,content,userid):
    session = so.Session(bind=engine)
    post = Post(title=title,description=content,user_id=userid)

    session.add(post)
    session.commit()
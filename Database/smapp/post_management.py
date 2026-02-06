import sqlalchemy as sa
import sqlalchemy.orm as so
from models import User, Post, Comment, Base

def view_posts_by_recency(engine):
    session = so.Session(bind=engine)


def view_posts_by_user(engine,uname):
    session = so.Session(bind=engine)

    qry = (sa.select(Post)
           .join(Post)
           .filter(User.name == uname))

    posts = session.scalars(qry).all()

    return posts

def make_post(engine,title,content,userid):
    session = so.Session(bind=engine)
    post = Post(title=title,description=content,user_id=userid)

    session.add(post)
    session.commit()
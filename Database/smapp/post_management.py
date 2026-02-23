import sqlalchemy as sa
import sqlalchemy.orm as so
import math
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

def post_exists(engine, postid):
    session = so.Session(bind=engine)
    qry = (sa.select(Post).filter(Post.id == postid))
    posts = session.scalars(qry).all()
    return len(posts) > 0


def view_posts_by_likes(engine):
    session = so.Session(bind=engine)

    qry = (sa.select(Post))

    posts = session.scalars(qry).all()

    tempposts = list(posts)

    sortedposts = []

    while len(tempposts) > 0:
        least_index = -1
        least_likes = math.inf
        for i in range(len(tempposts)):
            item = tempposts[i]
            if item.number_of_likes() < least_likes:
                least_likes = item.number_of_likes()
                least_index = i
        sortedposts.append(tempposts[least_index])
        tempposts.remove(tempposts[least_index])

    return sortedposts


def make_comment(engine,postid,username,comment):
    session = so.Session(bind=engine)
    useridqry = (sa.select(User.id).filter(User.name == username))

    userid = session.scalar(useridqry)

    newcomment = Comment(post_id=postid,user_id=userid,comment=comment)

    session.add(newcomment)
    session.commit()

def view_comments(engine,postid):
    session = so.Session(bind=engine)

    qry = (sa.select(Comment).filter(Comment.post_id==postid))
    comments = session.scalars(qry).all()
    return comments



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
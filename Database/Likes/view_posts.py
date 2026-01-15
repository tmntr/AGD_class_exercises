import sqlite3

def view_all_posts():
    try:
        with sqlite3.connect('soziales_medien.sqlite') as conn:
            cursor = conn.cursor()
            listofposts = '''
                select user.name, post.title,post.description
                from user, post
                where post.user_id = user.id;
                    '''

            # Execute the command
            cursor.execute(listofposts)
            results = cursor.fetchall()
            for row in results:
                print(row)

    except:
        print("Something went wrong")

def view_users_posts(name):
    try:
        with sqlite3.connect('soziales_medien.sqlite') as conn:
            cursor = conn.cursor()
            listofposts = '''
                select user.name, post.title,post.description
                from user, post
                where post.user_id = user.id
                and user.name = (?);
                    '''

            # Execute the command
            cursor.execute(listofposts,(name))
            results = cursor.fetchall()
            for row in results:
                print(row)

    except:
        print("Something went wrong")


def view_character_posts(name):
    try:
        with sqlite3.connect('soziales_medien.sqlite') as conn:
            cursor = conn.cursor()
            listofposts = '''select * from post
            where SUBSTR(description,-1,1) = '?' '''
            cursor.execute(listofposts,(name))
    except:
        print("Something went wrong")
running = True

while running:
    action = input("What would you like to do? Type 1 to view all posts\n2 to view a specific user's posts\n3 to view all posts ending in a certain character.")

    if action == '1':
        view_all_posts()
    elif action == '2':
        name = input("What is the name of the user you'd like to view? ")
        view_users_posts(name)
    elif action == '3':
        name = input("What character would you like to view? ")
        view_character_posts(name)


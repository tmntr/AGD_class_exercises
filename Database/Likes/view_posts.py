import sqlite3

def view_posts():
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

view_posts()


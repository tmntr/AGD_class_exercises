import sqlite3

def post_a_post(userid,title,content):
    try:
        with sqlite3.connect('soziales_medien.sqlite') as conn:
            cursor = conn.cursor()
            add_student = '''
                          INSERT INTO post (title, description, user_id)
                          VALUES (?, ?, ?); \
                          '''

            # Execute the command
            cursor.execute(add_student, (title,content,userid))

            conn.commit()
    except:
        print('Something went wrong')

userid = int(input('Enter userid: '))
title = input('Enter title: ')
content = input('Enter content: ')

post_a_post(userid,title,content)


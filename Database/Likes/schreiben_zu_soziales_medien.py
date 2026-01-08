import sqlite3

def program_to_add_user(uname,age=None,gender=None,nationality=None,bio=None):
    conn = sqlite3.connect('soziales_medien.sqlite')
    cursor = conn.cursor()
    add_student = '''
        INSERT INTO user (name, age, gender,nationality,bio)
            VALUES
                (?,?,?,?,?);
            '''

    # Execute the command
    cursor.execute(add_student, (uname, age, gender,nationality,bio))

    conn.commit()

    conn.close()

program_to_add_user("Tom",17)
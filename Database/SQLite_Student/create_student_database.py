import sqlite3

conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()

#Create a student table
create_students_table = '''
    CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER,
    gender TEXT
    );
        '''

#Execute the command
cursor.execute(create_students_table)

conn.close()

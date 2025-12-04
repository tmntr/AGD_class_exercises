import sqlite3

conn = sqlite3.connect('students.sqlite')
cursor = conn.cursor()

#Create a student table
def program_to_add_student(fname,sname,age,gender):
    add_student = '''
        INSERT INTO Students
            VALUES(fname,sname,age,gender)
        );
            '''

    #Execute the command
    cursor.execute(add_student)

name1 = input('Enter first name: ')
name2 = input('Enter last name: ')
age = int(input('Enter age: '))
gender = input('Enter gender: ')

program_to_add_student(name1,name2,age,gender)
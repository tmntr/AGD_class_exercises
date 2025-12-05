import sqlite3



#Create a student table
def program_to_add_student(fname,sname,age,gender):
    conn = sqlite3.connect('student.sqlite')
    cursor = conn.cursor()
    add_student = '''
        INSERT INTO students (first_name, last_name, age, gender)
            VALUES
                (?,?,?,?);
            '''

    # Execute the command
    cursor.execute(add_student, (fname, sname, age, gender))

    conn.commit()

    conn.close()



'''name1 = input('Enter first name: ')
name2 = input('Enter last name: ')
age = int(input('Enter age: '))
gender = input('Enter gender: ')

program_to_add_student(name1,name2,age,gender)

'''
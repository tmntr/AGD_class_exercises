import sqlite3

def program_to_add_user(uname,age=None,gender=None,nationality=None,bio=None):
    try:
        with sqlite3.connect('soziales_medien.sqlite') as conn:
            cursor = conn.cursor()
            add_student = '''
                INSERT INTO user (name, age, gender,nationality,bio)
                    VALUES
                        (?,?,?,?,?);
                    '''

            # Execute the command
            cursor.execute(add_student, (uname, age, gender,nationality,bio))

        conn.commit()
    except:
        print("Something went wrong")


name = input("Enter your username: ")

acceptedage = False
while not acceptedage:
    age = input("Enter your age(N/A if you wish to leave blank): ")
    if age.isnumeric():
        acceptedage = True
        age = int(age)
    elif age.upper() == "N/A":
        acceptedage = True
        age = None
    else:
        print("Please enter a valid integer age or N/A.")

acceptedgender = False
while not acceptedgender:
    gender = input("Enter your gender (N/A if you wish to leave blank): ")
    if gender in ["Male", "Female","Other"]:
        acceptedgender = True
    elif gender.upper() == "N/A":
        gender = None
    else:
        print("Please enter a valid gender or N/A.")

nationality = input("Enter your nationality (N/A if you wish to leave blank): ")
if nationality.upper() == "N/A":
    nationality = None

bio = input("Please enter a short bio if you wish (or N/A if you wish to leave blank): ")

if bio.upper() == "N/A":
    bio = None


program_to_add_user(uname=name,age=age,gender=gender,nationality=nationality,bio=bio)
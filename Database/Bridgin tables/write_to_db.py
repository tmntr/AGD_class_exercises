from sqlalchemy import create_engine

from sqlalchemy.orm import Session

from models import Person, Activity


# Create some instances of the Person class

people = [Person(first_name="Thomas", last_name="Noyce"),

Person(first_name="Colin", last_name="Laws"),

Person(first_name='Nutmeg', last_name="Lee"),

]


tda = Activity(name="3D animation")

cse = Activity(name="Computer science extension")

outdoor_ed = Activity(name="Outdoor Ed")


people[0].activities.append(cse)

people[0].activities.append(tda)

people[1].activities.append(tda)

people[2].activities.append(tda)



# Connect to the activities database

engine = create_engine('sqlite:///activities.sqlite', echo=True)


# Create a session and add the people to the database

with Session(engine) as sess:

    sess.add_all(people)

    sess.commit()
from sqlalchemy import create_engine

from sqlalchemy.orm import Session

from models import Person


# Create some instances of the Person class

tom = Person(first_name='Tom', last_name='Smith')

people = [Person(first_name="Jim", last_name="Jimson"), Person(first_name='Bim', last_name="Bimson"),Person(first_name='Roger', last_name="Rogers")]


# Connect to the activities database

engine = create_engine('sqlite:///newactivities.sqlite', echo=True)


# Create a session and add the people to the database

with Session(engine) as sess:

    sess.add(tom)

    sess.add_all(people)

    sess.commit()

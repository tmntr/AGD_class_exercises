from sqlalchemy import create_engine

from sqlalchemy.orm import Session

from models import Person

# Connect to the activities database

engine = create_engine('sqlite:///activities.sqlite', echo=True)

# sess = Session(engine)
# persons = sess.scalars(select(Person)).all()
# for person in persons:
#     person.greeting()
#     new_person = Person(first_name='Bob', last_name='Jones')
#     persons[0].last_name = "Smith"
#     sess.add(new_person)
#     sess.commit()
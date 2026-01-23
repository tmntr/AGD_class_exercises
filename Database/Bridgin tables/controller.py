import sqlalchemy as sa
import sqlalchemy.orm as so

from models import Person, Activity


class Controller:
    def __init__(self, db_location = 'sqlite:///activities.sqlite'):
        self.engine = sa.create_engine(db_location)

    def get_person_activities(self, first_name, last_name):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Person).where(Person.first_name == first_name and Person.last_name == last_name)
            user = session.scalar(stmt)
            activities = user.activities
            activity_names = [activity.name for activity in activities]
        return activity_names

    def get_people(self):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Person)
        return stmt


    def check_for_person(self,fname,lname):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Person).where(Person.first_name == fname and Person.last_name == lname)
            if len(stmt) > 0:
                return True
            else:
                return False


    def add_person(self,fname, lname):
        with so.Session(bind=self.engine) as session:
            new_person = Person(first_name=fname, last_name=lname)
            session.add(new_person)
            session.commit()



if __name__ == '__main__':
    controller = Controller()
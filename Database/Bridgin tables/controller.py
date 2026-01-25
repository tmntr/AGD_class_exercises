import sqlalchemy as sa
import sqlalchemy.orm as so

from models import Person, Activity


class Controller:
    def __init__(self, db_location = 'sqlite:///activities.sqlite'):
        self.engine = sa.create_engine(db_location)

    def get_activities(self):
        with so.Session(self.engine) as session:
            activitynames = session.query(Activity.name).all()
            return activitynames

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
            #print(stmt.execute())
            user = [session.scalar(stmt)]
            #print((session.scalar(stmt)))
            if len(user) > 0:
                return True
            else:
                return False

    def delete_person(self,fname,lname):
        with so.Session(bind=self.engine) as session:
            userget = sa.select(Person).where(Person.first_name == fname and Person.last_name == lname)
            user = session.scalar(userget)
            print(user)
            session.delete(user)
            session.commit()

    def add_person_to_activity(self,fname,lname,activityname: str):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Activity).where(Activity.name == activityname)
            activity = session.scalar(stmt)
            getuser = sa.select(Person).where(Person.first_name == fname and Person.last_name == lname)
            user = session.scalar(getuser)
            activity.attendees.append(user)
            user.activities.append(activity)
            session.commit()



    def add_person(self,fname, lname):
        with so.Session(bind=self.engine) as session:
            new_person = Person(first_name=fname, last_name=lname)
            session.add(new_person)
            session.commit()

    def change_name(self,fname,lname,nfname,nlname):
        with so.Session(bind=self.engine) as session:
            # nameedit = sa.update(Person).where(Person.first_name == fname and Person.last_name == lname).set(first_name=nfname, last_name=nlname)
            # session.execute(nameedit)
            personget = sa.select(Person).where(Person.first_name == fname and Person.last_name == lname)
            person = session.scalar(personget)
            person.first_name = nfname
            person.last_name = nlname
            session.commit()

    def delete_person_activity(self,fname,lname,activityname: str):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Activity).where(Activity.name == activityname)
            activity = session.scalar(stmt)
            userget = sa.select(Person).where(Person.first_name == fname and Person.last_name == lname)
            user = session.scalar(userget)
            activity.attendees.remove(user)
            #user.activities.remove(activity)
            session.commit()

    def delete_activity(self,activityname: str):
        with so.Session(bind=self.engine) as session:
            activityget = sa.select(Activity).where(Activity.name == activityname)
            activity = session.scalar(activityget)
            session.delete(activity)
            session.commit()

    def edit_activity(self,currentname,newactivityname: str):
        with so.Session(bind=self.engine) as session:
            activityget = sa.select(Activity).where(Activity.name == newactivityname)
            activity = session.scalar(activityget)
            activity.name = newactivityname
            session.commit()

    def add_activity(self,activityname: str):
        with so.Session(bind=self.engine) as session:
            newactivity = Activity(name=activityname)
            session.add(newactivity)
            session.commit()


    def get_attendees(self,activityname: str):
        with so.Session(self.engine) as session:
            activityget = sa.select(Activity).where(Activity.name == activityname)
            activity = session.scalar(activityget)
            return activity.attendees

    # def delete_person(self,fname,lname):
    #     with so.Session(bind=self.engine) as session:
    #         pass
    #         session.delete(Person)




if __name__ == '__main__':
    controller = Controller()
# import pyinputplus as pyip

from controller import Controller

class CLI:
    def __init__(self):
        self.controller = Controller()

    def show_activities(self):
        activities = self.controller.get_activities()
        for activity in activities:
            print(activity)

    def show_person_activities(self):
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        activities = self.controller.get_person_activities(first_name, last_name)
        for activity in activities:
            print(activity)

    def add_person_activities(self):
        first_name = input('Enter the first name: ')
        last_name = input('Enter the last name: ')
        activity = input('Enter your desired activity: ')
        #exists = self.controller.check_for_person(first_name, last_name)
        #if exists:
        #    print('Someone with that name already exists.')#, are you sure? (y/n)\n')
            # if input().lower() == 'y':
            #     self.controller.add_person(first_name, last_name)
            # else:
            #     print('Fair enough.')
        #else:
        self.controller.add_person_to_activity(first_name, last_name, activity)

    def add_person(self):
        first_name = input('Enter the first name: ')
        last_name = input('Enter the last name: ')
        self.controller.add_person(first_name, last_name)

    def edit_name(self):
        first_name = input('Enter the current first name: ')
        last_name = input('Enter the current last name: ')
        newfname = input('Enter the new first name: ')
        newlname = input('Enter the new last name: ')
        self.controller.edit_person(first_name, last_name, newfname, newlname)

    def delete_person(self):
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        self.controller.delete_person(first_name, last_name)

    def delete_person_activity(self):
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        activity = input('Enter your the activity name: ')
        self.controller.delete_person_activity(first_name, last_name,activity)

    def delete_activity(self):
        activity = input('Enter your desired activity: ')
        self.controller.delete_activity(activity)

    def add_activity(self):
        newactivity = input('Enter the name of the new activity: ')
        self.controller.add_activity(newactivity)

    def edit_activity(self):
        currentname = input('Enter your desired activity: ')
        newactivity = input('Enter the new name for your desired activity: ')
        self.controller.edit_activity(currentname, newactivity)

    def get_attendees(self):
        activityname = input('Enter your desired activity: ')
        attendees = self.controller.get_attendees(activityname)
        for attendee in attendees:
            print(attendee.first_name +' '+ attendee.last_name)


    def menu(self):
        print('Please choose from the following options:')
        print('1. List available activities\n2. List a specific person\'s activities\n3.Add person\n4. Edit person\n5. Delete person\n6. Enroll a person in an activity\n7. Remove someone from an activity\n8. Remove an activity\n9. Add an activity\n10. Edit an activity\n11. View an activity\'s attendees.')
        action = input()
        if action == '1':
            self.show_activities()
        elif action == '2':
            self.show_person_activities()
        elif action == '3':
            self.add_person()
        elif action == '4':
            self.edit_name()
        elif action == '5':
            self.delete_person()
        elif action == '6':
            self.add_person_activities()
        elif action == '7':
            self.delete_person_activity()
        elif action == '8':
            self.delete_activity()
        elif action == '9':
            self.add_activity()
        elif action == '10':
            self.edit_activity()
        elif action == '11':
            self.get_attendees()
        else:
            print('That was not an option. Please try again.')

if __name__ == '__main__':
    cli = CLI()

while True:
    cli.menu()
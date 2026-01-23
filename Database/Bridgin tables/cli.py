# import pyinputplus as pyip

from controller import Controller

class CLI:
    def __init__(self):
        self.controller = Controller()

    def show_person_activities(self):
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        activities = self.controller.get_person_activities(first_name, last_name)
        for activity in activities:
            print(activity)
    def add_person_activities(self):
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        exists = self.controller.check_for_person(first_name, last_name)
        if exists:
            print('Someone with that name already exists, are you sure? (y/n)\n')
            if input().lower() == 'y':
                self.controller.add_person(first_name, last_name)
            else:
                print('Fair enough.')
        else:
            self.controller.add_person(first_name, last_name)

    def menu(self):
        print('Please choose from the following options:')
        print('1. List available activities\n2. List a specific person\'s activities\n3.Add person')
        action = input()
        if action == '1':
            self.show_person_activities()
        elif action == '2':
            self.add_person_activities()
        elif action == '3':
            self.add_person_activities()
        else:
            print('That was not an option. Please try again.')

if __name__ == '__main__':
    cli = CLI()

while True:
    cli.show_person_activities()
import sqlite3
from faker import Faker
from write_to_db import program_to_add_student
import random
fake = Faker('en_UK')


for _ in range(10):
    fakeygender = ['Male', 'Female'][random.randint(0, 1)]
    if fakeygender == 'Female':
        fakeyfname = fake.first_name_female()
        fakeylname = fake.last_name_female()
    elif fakeygender == 'Male':
        fakeyfname = fake.first_name_male()
        fakeylname = fake.last_name_male()

    fakeyage = random.randint(16,17)

    program_to_add_student(fakeyfname,fakeylname,fakeyage,fakeygender)

import sqlite3

def createcustomerfile():
    conn = sqlite3.connect('customer.sqlite')
    cursor = conn.cursor()

    # Create a student table
    create_customers_table = '''
                            CREATE TABLE IF NOT EXISTS customers
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              first_name TEXT NOT NULL, last_name TEXT NOT NULL, 
                             address TEXT NOT NULL
                            );'''

    # Execute the command
    cursor.execute(create_customers_table)

    conn.close()

def createtracklistfile():
    conn = sqlite3.connect('tracklist.sqlite')
    cursor = conn.cursor()

    # Create a student table
    create_tracklist_table = '''
                            CREATE TABLE IF NOT EXISTS tracklist
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              track_name TEXT NOT NULL, artist_name TEXT NOT NULL, 
                             track_length INTEGER NOT NULL
                            );'''

    # Execute the command
    cursor.execute(create_tracklist_table)

    conn.close()

def createcityfile():
    conn = sqlite3.connect('city.sqlite')
    cursor = conn.cursor()

    # Create a student table
    create_city_table = '''
                            CREATE TABLE IF NOT EXISTS city
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              city TEXT NOT NULL, 
                             population INTEGER NOT NULL
                            );'''

    # Execute the command
    cursor.execute(create_city_table)

    conn.close()
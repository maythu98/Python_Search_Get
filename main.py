import sys
import sqlite3
from sqlite3 import Error

# Connect With Database
try:
    db = sqlite3.connect('mydatabase.db')

    db.execute("CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(255), name VARCHAR(255), INDEX(title, name))")
    
except Error:
    print(Error)


def main():

    # identify main value      
    insert = 1
    search = 2
    main_val = 2

    argv = sys.argv
    if (len(argv) < 2):
        # Get input From User
        main_val = input("Please Type 1 if you want to insert data. Or type 2 if you want to search. 1/2:")
        main_val = userInputErrorHandling(main_val)
        
        while main_val not in [insert, search]:
            main_val = input("Please Type 1 or 2:")
            main_val = userInputErrorHandling(main_val)


    if (len(argv) >= 2):
        arg = argv[1]

        if arg in ['s', 'ss', 'search', 's-']:
            main_val = 2

        if arg in ['i', 'i-', 'insert', 'insert-']:
            main_val = 1

    # Search Features
    if (main_val == search):
        # Search From DB
        if (len(argv) == 3):
            val = argv[2]
        else:
            val = input("Type Search Name:")

        searchData(val)


    # Insert Data
    if (main_val == insert):
        if (len(argv) == 4):
            title = argv[2]
            name = argv[3]
        else:
            title = input("Type Title: ")
            name = input("Type Name: ")
        insertData(title, name)


def userInputErrorHandling(val):
    try:
        val = int(val)
    except:
        print("Invalid Error, Please try Again")
        val = int(3)

    return val


def insertData(title, name):
    # insert data
    db.execute("INSERT INTO notes (title, name) VALUES (:title, :name)", {"title": title, "name": name})
    db.commit()
    print("I am inserted!", title, name)



def searchData(val):
    # search with data
    result = db.execute("SELECT * FROM notes WHERE title LIKE :value", {"value": '%'+val+'%'})
    rows = result.fetchall()
    if len(rows) < 1:
        print("Nothing...")
        return 1
    
    for row in rows:
        print(row[1], '====>' ,row[2])


main()
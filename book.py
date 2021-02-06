import sys
import sqlite3
import argparse

db = sqlite3.connect('phonebookDB.sqlite')
c = db.cursor()

class Phonebook(object):
    def __init__(self):
        try:
            c.execute('CREATE TABLE entries(id INTEGER PRIMARY KEY, name TEXT, phone TEXT unique)')
        except:
            pass

    def addEntry():
        name = input('Please, enter a name: ')
        number = input('Please, enter a number: ')
        c.execute('INSERT INTO entries(name, phone) VALUES(?,?)', (name, number))
        db.commit()

    def delEntry():
        name = input('Please, enter a name to delete: ')
        c.execute('DELETE FROM entries WHERE name=?', [name])
        db.commit()

    def query():
        c.execute('SELECT name, phone FROM entries')
        for items in c:
            print(items)

    def exit():
        sys.exit()#можно break

Phonebook()

parser = argparse.ArgumentParser(description='Phonebook')
parser.add_argument('-q', '--query', action='store_true', help='show all existing contacts')
parser.add_argument('-e', '--exit', action='store_true', help='just exit from program')
parser.add_argument('-a', '--add', action='store_true', help='add a new contact')
parser.add_argument('-d', '--delete', action='store_true', help='delete a contact')
args = parser.parse_args()
parser.print_help()
print('-----------------------------------')

if args.query:
    Phonebook.query()
   
if args.exit:
    Phonebook.exit()

if args.add:
    Phonebook.addEntry()

if args.delete:
    Phonebook.delEntry()

db.close()
#!/usr/bin/python

import sqlite3
conn = sqlite3.connect('todo.db')

c = conn.cursor()

c.execute('''CREATE TABLE todos
             (id INTEGER PRIMARY KEY, title TEXT, is_completed BOOLEAN)''')

# Insert a row of data
c.execute("INSERT INTO todos VALUES ('1', 'do something awesome', 'true')")
#c.execute("INSERT INTO todos VALUES ('2', 'do something awesomer', 'true')")
#c.execute("INSERT INTO todos VALUES ('3', 'do something awesomest', 'true')")

conn.commit()
conn.close()
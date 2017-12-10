import sqlite3

conn = sqlite3.connect('recommender.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE user1
         (uid    INTEGER PRIMARY KEY  AUTOINCREMENT,
         username       TEXT(50)  NOT NULL,
         password       VARCHAR(100)  NOT NULL,
         email        TEXT(50)  NOT NULL);''')
print ("Table created successfully");

conn.close()
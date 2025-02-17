# import sqlite to be able to work with it
import sqlite3

# import the database object to be ran
from Database import Database

# make database object on our sql database
db = Database("stock_db.db")

# run initial data code (the sql file)
db.initial_table()

# run main program and then close the connection
db.run()
db.close()










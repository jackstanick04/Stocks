# import sqlite to be able to work with it
import sqlite3

# import the database object
from Database import Database

# make database object and test methods
db = Database("stock_db.db")
db.clear()
db.initial_table()
db.test_method()







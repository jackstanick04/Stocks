# import sqlite to be able to work with it
import sqlite3

# import the database object
from Database import Database

# make database object and test methods
db = Database("stock_db.db")
db.initial_table()
db.print_table("companies")
db.print_table("shares")
db.close()







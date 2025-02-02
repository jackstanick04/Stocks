# edit all of this as we get specifics

# import sqlite
import sqlite3

# instanciate the class
class Database :

    # constructor method (just makes the connect and cursor)
    def __init__ (self, name_db) :
        self.connect = sqlite3.connect(name_db)
        self.cursor = self.connect.cursor()

    # clear table so data does not continue stacking (temporary)
    def clear (self) :
        self.cursor.execute("DELETE FROM test")
        self.connect.commit()
    
    # code to set up the initial table
    def initial_table (self) :
        # read the sql script file and set up the db with predfined sql code
        with open("stock_db.sql", "r") as sql_file:
            sql_data = sql_file.read()
        # have the cursor execute the prewritten script and then connect and update to the database
        self.cursor.executescript(sql_data)
        self.connect.commit

    # test method to see if we can link python and sql (we can)
    def test_method (self) :
        # select and store initial data from database
        self.cursor.execute("SELECT * FROM test")
        initial = self.cursor.fetchall()

        self.print_table("test")

        # execute a change that modifies the table (insert row) so needs to be committed to data base
        self.cursor.execute("INSERT INTO test (name) VALUES ('Kate')")
        self.connect.commit()

        # store the next table
        self.cursor.execute("SELECT * FROM test")
        second = self.cursor.fetchall()

        self.print_table("test")
    
    # closes connect
    def close (self) :
        self.connect.close()

    # print method just as tuples for rows (not pretty)
    def print_table (self, table_name) :
        # use string formatting to get the query (curly braces and f are types of formatting)
        table = f"SELECT * FROM {table_name}"
        # execute and store the selec
        self.cursor.execute(table)
        rows = self.cursor.fetchall()

        # loop through every row of tuples and print
        for row in rows :
            print(row)




    
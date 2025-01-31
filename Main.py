# import sqlite to be able to work with it
import sqlite3

# establish a connection (able to make modifications and acces) and a cursor (able to execute queries)
connect = sqlite3.connect("stock_db.db")
cursor = connect.cursor()

# delete data so not runs dont continually add
cursor.execute("DELETE FROM test")
connect.commit()

# read the sql script file and set up the db with predfined sql code
with open("stock_db.sql", "r") as sql_file:
    sql_data = sql_file.read()
# have the cursor execute the prewritten script and then connect and update to the database
cursor.executescript(sql_data)
connect.commit

# select and store initial data from database
cursor.execute("SELECT * FROM test")
initial = cursor.fetchall()

# execute a change that modifies the table (insert row) so needs to be committed to data base
cursor.execute("INSERT INTO test (name) VALUES ('Kate')")
connect.commit()

# store the next table
cursor.execute("SELECT * FROM test")
second = cursor.fetchall()

print(initial)
print(second)

# always close connection
connect.close()





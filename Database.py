# edit all of this as we get specifics

# import sqlite
import sqlite3

# instanciate the class
class Database :

    # constructor method (just makes the connect and cursor)
    def __init__ (self, name_db) :
        self.connect = sqlite3.connect(name_db)
        self.cursor = self.connect.cursor()
    
    # code to set up the initial table
    def initial_table (self) :
        # read the sql script file and set up the db with predfined sql code
        with open("stock_db.sql", "r") as sql_file:
            sql_data = sql_file.read()
        # have the cursor execute the prewritten script and then connect and update to the database
        self.cursor.executescript(sql_data)
        self.connect.commit()
    
    # closes connect
    def close (self) :
        self.connect.close()

    # print method with column names 
    def print_pretty (self) :
        # fixed width for each column
        width = 18

        # store the column names in a list with list comprehension (the cursor execute will store the desired table (in main), and then the first element of every column description is the name of the column)
        column_names = [desc [0] for desc in self.cursor.description]
        # formatting the column names using ljust (fills with extra spaces to twelve for every column in the column array) and then joining each
        col_names = "".join([col_new.ljust(width) for col_new in column_names])
        print("\n" + col_names + "\n")
        
        # store list of every tuple of table using fetchall 
        rows = self.cursor.fetchall()
        # formatting each row same idea just with a loop
        for row in rows :
            # each row joins each value of the tuple casted as a string with appropriate spacing
            new_row = "".join([str(val).ljust(width) for val in row])
            print(new_row)
        print()

    # function to run the program
    def run (self) :
        # have a flag variable for the loop to run on (only turns false when they exit)
        flag = True
        while flag :
            # take in user input as a string
            print("-1 : Quit. 1 : Analyze one company. 2 : Analyze two companies. 3 : Analyze all companies.")
            choice = input("Please enter your choice: ")

            # all comparisons will be with strings since input takes in strings
            # if -1 exit the loop by inverting the flag
            if choice == "-1" : 
                print("Exiting the program.")
                flag = False
            # elif for the different db methods to run
            elif choice == "1" : 
                self.oneComp()
            elif choice == "2" : 
                self.twoComp()
            elif choice == "3" : 
                self.allComp()
            # else to rerun the loop with no action because invalid input
            else : 
                print("Please enter valid input.")
        
    # general function for one company
    def oneComp (self) :
        print("One Company")
    
    # general function for two companies
    def twoComp (self) :
        print("Two Companies")
    
    # general function for one company
    def allComp (self) :
        print("All Companies")

        




    
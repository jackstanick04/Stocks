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

    # print method with column names (works for any selected data table that is stored in the cursor)
    def print_pretty_all (self) :
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
       # ask the user for which company they would like to operate on
       self.print_companies()
       # oppurtunity to validate input
       company = int(input("Please enter the company id: ")) 

       # take in the user action option; can be updated to add input validation
       self.print_options_one()
       choice = int(input("Selection: "))

       # after they enter which task, call an appropriate method on the task to complete (this is like a switch in java)
       match choice :
            case 1 : 
               # take in the year and then call method; spot to validate input
               year = int(input("What year would you like to see (2015 - 2024): "))
               self.prices_one_year(company, year)
            case 2 :
               # call method to see prices for every year
               self.prices_one_all(company)
            case 3 :
               # call method to see average stock price
               self.avg_one(company)
            case 4 :
               # call method to see maximum stock price
               self.max_one(company)
            case 5 :
               # call method to see minimum stock price
               self.min_one(company)
            case 6 :
               # call method to see standard deviation of stock prices
               self.std_one(company)
            case 7 :
               # call method to see the yearly increase/decrease
               self.inc_one(company)
            case 8 :
               # call method to rank highest price years
               self.rank_one(company)
            case _ :
               print("Invalid. Ending selection process.")
               
    def print_companies (self) :
        # query to just have the company id and the company name
        query = """
        SELECT id,
            name,
            ticker
        FROM companies"""
        # execute the query and print it (print will do the current thing stored in cursor (which is the execution))
        self.cursor.execute(query)
        self.print_pretty_all()
    
    # prints the different options that method one can do
    def print_options_one (self) :
        print("\nPlease enter the number that corresponds to what you would like to do: ")
        print("1. See stock prices for one year.")
        print("2. See stock prices for all years.")
        print("3. See average stock price.")
        print("4. See maximum stock price.")
        print("5. See minimum stock price.")
        print("6. See standard deviation of stock prices.")
        print("7. See yearly increase/decrease of stock prices.")
        print("8. See rank of highest price years.")

    # takes in the company and year and prints and ticker, year, and rounded price for that year
    def prices_one_year (self, company_id, year) :
        # string query, just selecting entry with matching year and company (see avg_one for the placeholder explanation)
        query = """
        SELECT companies.ticker, 
            shares.year,
            ROUND(shares.price, 2)
        FROM shares
        JOIN companies
            ON shares.company_id = companies.id
        WHERE shares.company_id = ?
            AND shares.year = ?
        """
        # execute query with placeholders and print
        self.cursor.execute(query, (company_id, year))
        self.print_pretty_all()

    # selects and prints the ticker, year, and rounded price for all years of one company
    def prices_one_all (self, company_id) :
        # string query to select all shares of a given company
        query = """
        SELECT companies.ticker,
            shares.year,
            ROUND(shares.price, 2)
        FROM shares
        JOIN companies
            ON shares.company_id = companies.id
        WHERE shares.company_id = ?
        """
        # execute and print
        self.cursor.execute(query, (company_id,))
        self.print_pretty_all()
        
    
    # takes in a company id and prints the ticker and rounded price
    def avg_one (self, company_id) :
        # execute the average command using a place holder (?) for the python company parameter
        # join the tables for proper output on primary/foreign key and group by the company id to select the average
        query = """
        SELECT companies.ticker,
            ROUND(AVG(shares.price), 2) AS 'Average Price'
        FROM shares
        JOIN companies
            ON shares.company_id = companies.id
        WHERE shares.company_id = ?
        GROUP BY companies.id"""
        # execute the query and print, no need to return since the cursor instance variable stores the desired results
        self.cursor.execute(query, (company_id,))
        self.print_pretty_all()

    # selects and prints the ticker, year, and maximum price of a company
    def max_one (self, company_id) :
        # query to select max, group by ticker (company)
        query = """
        SELECT companies.ticker,
            shares.year,
            MAX(shares.price)
        FROM shares
        JOIN companies
            ON shares.company_id = companies.id
        WHERE shares.company_id = ?
        GROUP BY 1
        """
        self.cursor.execute(query, (company_id,))
        self.print_pretty_all()

    # same code as max just a different aggregate function
    def min_one (self, company_id) :
        query = """
        SELECT companies.ticker,
            shares.year,
            MIN(shares.price)
        FROM shares
        JOIN companies
            ON shares.company_id = companies.id
        WHERE shares.company_id = ?
        GROUP BY 1
        """
        self.cursor.execute(query, (company_id,))
        self.print_pretty_all()

    def std_one (self, company_id) :
        print("std one")

    def inc_one (self, company_id) :
        print("inc one")

    def rank_one (self, company_id) :
        print("rank one")

    # general function for two companies
    def twoComp (self) :
        print("Two Companies")
    
    # general function for one company
    def allComp (self) :
        print("All Companies")

        




    
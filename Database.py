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
               print(self.prices_one_year(company, year))
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
        # store and return the value
        result = self.cursor.fetchone()
        self.print_pretty_all()
        return result [0]

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

    # code for standard deviation
    def std_one (self, company_id) :
        # query utilizes a subquery to have a table of all prices and the average price for all years in the given company
        # outside query then performs a sum of all prices - average quantity squarred, then divides and takes square root for the std 
        query = """
        SELECT companies.ticker,
            ROUND ( SQRT ( SUM ( (price - avg_price) * (price - avg_price) ) / (COUNT(*) - 1) ), 2 ) AS std_deve
        FROM (
            -- get price for every share in the company id
            SELECT price,
                -- subquery to find the average price from the given company id
                (SELECT AVG(price) AS 'avg_price' FROM shares WHERE company_id = ?) AS avg_price
            FROM shares
            WHERE company_id = ?
        ) AS avg_finder
        -- joining comapnies where the company id is the desired id only (dont really need to do it for other entries)
        JOIN companies
            ON companies.id = ?
        """
        self.cursor.execute(query, (company_id, company_id, company_id))
        self.print_pretty_all()
        
    # method to show the dollar and percent increase 
    def inc_one (self, company_id) :
        query = """
        -- select the ticker, year, price, dollar increase, percent increase
        SELECT companies.ticker,
            shares.year,
            shares.price,
            -- lag function to find change in price
            ROUND((shares.price - LAG(shares.price) OVER (PARTITION BY shares.company_id ORDER BY shares.year)), 2) AS dollar_increase,
            -- longer use of lag functions to find percent change (difference divided by previous price)
            ROUND(((shares.price - LAG(shares.price) OVER (PARTITION BY shares.company_id ORDER BY shares.year)) / 
                LAG(shares.price) OVER (PARTITION BY shares.company_id ORDER BY shares.year)) * 100, 2) AS percent_increase
        FROM shares
        JOIN companies
            ON shares.company_id = companies.id
        WHERE shares.company_id = ?
        """
        self.cursor.execute(query, (company_id,))
        self.print_pretty_all()

    # rank function not too hard 
    def rank_one (self, company_id) :
        query = """
        -- data to be selected
        SELECT companies.ticker,
            -- ranked descending, partitioned by company, and order by price
            RANK() OVER (PARTITION BY shares.company_id ORDER BY shares.price DESC) AS price_rank,
            shares.year,
            shares.price
        FROM shares
        -- joined and only the desired company
        JOIN companies
            ON shares.company_id = companies.id
        WHERE shares.company_id = ?
        """
        self.cursor.execute(query, (company_id,))
        self.print_pretty_all()

    # general function for two companies
    def twoComp (self) :
        # print and take in the company ids; oppurtunity to validate user input
        self.print_companies()
        comp_one = int(input("Please enter your first company id: "))
        comp_two = int(input("Please enter your second company id: "))

        # print the options and take in the choice
        self.print_options_two()
        choice = int(input("Please enter the action you would like: "))

        # match statement on the choice to call each given method
        match choice :
            case 1 :
                # take year in and then call method to find higher price in given year; validate input
                year = int(input("Please enter the given year: "))
                self.higher_two(year, comp_one, comp_two)
            case 2 :
                # method to find higher average price
                self.avg_two(comp_one, comp_two)
            case 3 :
                # method to find higher standard deviation
                self.std_two(comp_one, comp_two)
            case 4 :
                # method to find higher max price
                self.max_two(comp_one, comp_two)
            case 5 :
                # method to find lower min price
                self.min_two(comp_one, comp_two)
            case _ :
                # default (not right input)
                print("Invalid input. Ending selection process.")

    # prints the different options that the two company method can call
    def print_options_two (self) :
        print("\nPlease enter the number that corresponds to what you would like to do between two companies: ")
        print("1. Find the higher price for a given year.")
        print("2. Find the higher average price.")
        print("3. Find the higher standard deviation.")
        print("4. Find the higher maximum price.")
        print("5. Find the lower minimum price.")

    # method to find higher price in given year
    def higher_two (self, year, comp_one, comp_two) :
        # sql query
        query = """
        -- temprorary table to find the max prices for the given comapnies in the year
        WITH max_prices AS (
            -- select desired data from joined table
            SELECT companies.ticker,
                shares.year,
                shares.price
            FROM shares
            JOIN companies
                ON shares.company_id = companies.id
            -- filter to only the price with the given year or company
            WHERE year = ? AND (shares.company_id = ? OR shares.company_id = ?) 
        )
        SELECT ticker,
            year,
            price
        FROM max_prices
        -- way to take the max price
        ORDER BY 3 DESC
        LIMIT 1
        """
        self.cursor.execute(query, (year, comp_one, comp_two))
        self.print_pretty_all()
    
    # method to find higher average price 
    def avg_two (self, comp_one, comp_two) :
        # average query with comments within
        query = """
        -- temporary table, selects the company id and the average price (grouped on company id) for the desired companies
        WITH avg_prices AS (
            SELECT company_id,
                AVG(price) AS avg_price
            FROM shares
            WHERE company_id = ? OR company_id = ?
            GROUP BY company_id
        )
        -- select and join the companies table for ticker, and then the average price only for the max average price from the subquery (shown in bottom line)
        SELECT companies.ticker,
            avg_prices.avg_price
        FROM avg_prices
        JOIN companies
            ON avg_prices.company_id = companies.id
        WHERE avg_prices.avg_price = (SELECT MAX(avg_price) FROM avg_prices)
        """
        self.cursor.execute(query, (comp_one, comp_two))
        self.print_pretty_all()

    # method to find the greater standard deviation
    def std_two (self, comp_one, comp_two) :
        # sql query, uses multiple subqueries
        query = """
        -- table to find the means and company id for the given companeis
        WITH means AS (
            SELECT shares.company_id,
                AVG(shares.price) AS mean
            FROM shares
            WHERE shares.company_id = ? OR shares.company_id = ?
            GROUP BY 1
        ),
        -- table to find standard deviations
        stds AS (
            SELECT shares.company_id,
                --calculation (we know formula, basically just uses the joined row to get the price and mean)
                ROUND( SQRT (SUM ( (shares.price - means.mean) * (shares.price - means.mean) ) / (COUNT(*) - 1) ), 2 ) AS std
            FROM shares
            -- joining so every row has both the current price and the mean
            JOIN means
                ON shares.company_id = means.company_id
            WHERE shares.company_id = ? OR shares.company_id = ?
            GROUP BY shares.company_id
        )
        -- select the std and then the company ticker by joining the companies table on the stds table where company id are equal
        SELECT companies.ticker,
            stds.std
        FROM stds
        JOIN companies
            ON stds.company_id = companies.id
        -- only take highest
        ORDER BY 2 DESC
        LIMIT 1
        """
        self.cursor.execute(query, (comp_one, comp_two, comp_one, comp_two))
        self.print_pretty_all()

    # method to find the higher max price
    def max_two (self, comp_one, comp_two) :
        # sql query, similar to the higher price of a given year
        query = """
        -- subquery to find the max price for the given companies
        WITH maxes AS (
            -- taking joined ticker from companies and max price from the desired tables using group
            SELECT companies.ticker,
                MAX(shares.price) AS max
            FROM shares
            JOIN companies
                ON shares.company_id = companies.id
            WHERE shares.company_id = ? OR shares.company_id = ?
            GROUP BY shares.company_id
        )
        SELECT ticker,
            max
        FROM maxes
        -- only take the highest
        ORDER BY max DESC
        LIMIT 1
        """
        self.cursor.execute(query, (comp_one, comp_two))
        self.print_pretty_all()

    # method to find the lower min price
    def min_two (self, comp_one, comp_two) :
        # nearly identical to the find max, just finding each minimum and selecting lower from there
        query = """
        -- subquery to find the max price for the given companies
        WITH mins AS (
            -- taking joined ticker from companies and min price from the desired tables using group
            SELECT companies.ticker,
                MIN(shares.price) AS min
            FROM shares
            JOIN companies
                ON shares.company_id = companies.id
            WHERE shares.company_id = ? OR shares.company_id = ?
            GROUP BY shares.company_id
        )
        SELECT ticker,
            min
        FROM mins
        -- only take the lowest
        ORDER BY min
        LIMIT 1
        """
        self.cursor.execute(query, (comp_one, comp_two))
        self.print_pretty_all()

    # general function for one company
    def allComp (self) :
        # no need to take company choice input, rather just print and selec the desired task
        self.print_options_all()
        choice = int(input("Please enter your selection: "))

        # match statement based on choice; oppurtunity to validate input
        match choice :
            case 1 :
                # method for average rank
                self.avg_all()
            case 2 :
                # method for std rank
                self.std_all()
            case 3 :
                # method for highest prices rank
                self.highest_all_all()
            case 4 :
                # input and method to rank prices in a given year; chance to validate input
                year = int(input("Please enter a year: "))
                self.highest_all_year(year)
            case _ :
                # default
                print("Invalid choice, ending program.")

    # function to print all company options
    def print_options_all (self) :
        print("\nPlease select the option that you would like to complete: ")
        print("1. Rank the average stock prices.")
        print("2. Rank the standard deviations.")
        print("3. Rank the highest price for each company across all years.")
        print("4. Rank the prices for each company in a given year.")
    
    # method for ranking average of all, no company id paramter needed
    def avg_all (self) :
        # query for avg prices
        query = """
        -- temporary table which holds the average price for every company
        WITH avg_prices AS (
            SELECT company_id,
                AVG(price) AS avg
            FROM shares
            GROUP BY 1
        )
        -- rank by the average prices, and select the tickers and rounded price
        SELECT RANK () OVER (ORDER BY avg DESC) AS ranking,
            companies.ticker,
            ROUND(avg_prices.avg, 2) AS avg
        FROM avg_prices
        JOIN companies
            ON avg_prices.company_id = companies.id
        """
        
        # execute commands
        self.cursor.execute(query)
        self.print_pretty_all()

    # method for ranking std of all, no company id paramter needed
    def std_all (self) :
        # query for standard deviation, very similar to the two company version
        query = """
        -- temporary table to store the average of each company
        WITH avgs AS (
            SELECT company_id,
                AVG(price) AS avg
            FROM shares
            GROUP BY 1
        ),
        stds AS (
            -- select the company id, and std
            SELECT shares.company_id,
                ROUND ( SQRT ( SUM ( (shares.price - avgs.avg) * (shares.price - avgs.avg) ) / (COUNT(*) - 1) ), 2 ) AS std
            FROM avgs
            -- basically gives every price the average for the given company next to it, which we then sum the deviations per each company to calculate
            JOIN shares
                ON avgs.company_id = shares.company_id
            GROUP BY 1
        )
        -- just rank the deviations descending
        SELECT RANK () OVER (ORDER BY std DESC) AS rank,
            companies.ticker,
            stds.std
        FROM stds
        JOIN companies
            ON stds.company_id = companies.id
        """

        # execute and print
        self.cursor.execute(query)
        self.print_pretty_all()

    # method for highest prices across all years, no company id needed
    def highest_all_all (self) :
        print("highest")

    # method for ranking across a year, year is the only paramters needed
    def highest_all_year (self, year) :
        print(year)

        




    
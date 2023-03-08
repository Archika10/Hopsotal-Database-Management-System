Hospital Database Management System
This is a simple Hospital Database Management System created using Python and PostgreSQL. The system allows you to create, retrieve, update, and delete data from the database using Python code.

## Prerequisites:
Python 3.x


psycopg2 library for Python


PostgreSQL database server

## Setup:
Clone the repository using git clone <repository URL>
Install the required dependencies using pip install -r requirements.txt
Create a PostgreSQL database and update the DATABASE_URI in config.py
Create the necessary tables in the database using python main.py --action create
Run the system using the command python main.py
  
## Usage:
The system provides four main functions to interact with the database:
create_data_table(queries: List[str]): Creates tables in the database based on the provided SQL queries.
  
  
insert_data_table(queries: List[str]): Inserts data into the tables in the database based on the provided SQL queries.
  
  
update_data_table(queries: List[str]): Updates data in the tables in the database based on the provided SQL queries.
  
  
delete_data_table(queries: List[str]): Deletes data from the tables in the database based on the provided SQL queries.
  
  
To use these functions, simply call them with a list of SQL queries as arguments. For example, to create a new table in the database:
'''
from helper import DatabaseHelper

# Initialize the database helper object
db = DatabaseHelper()

# Define the SQL query to create the new table
query = "CREATE TABLE new_table (id SERIAL PRIMARY KEY, name VARCHAR(50));"

# Call the create_data_table function with the query
db.create_data_table([query])
'''  
  
Similarly, you can use the other functions to interact with the database as per your requirements.
  
## Contribution:
Contributions to this project are welcome. Please submit a pull request or open an issue to get started.

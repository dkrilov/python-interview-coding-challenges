# Challenge 1: SQLite Database Connection
# Write a Python code snippet that demonstrates establishing a connection to an SQLite database and executing a query to retrieve data.
# Example:
# (See code for usage)
import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM users")

# Fetch all rows
rows = cursor.fetchall()

# Print the data
for row in rows:
    print(row)

# Close the cursor and the connection
cursor.close()
conn.close()

# Challenge 2: MySQL Database Connection
# Write a Python code snippet that demonstrates establishing a connection to a MySQL database and executing a query to retrieve data.
# Example:
# (See code for usage)
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="example"
)

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM users")

# Fetch all rows
rows = cursor.fetchall()

# Print the data
for row in rows:
    print(row)

# Close the cursor and the connection
cursor.close()
conn.close()

# Challenge 3: PostgreSQL Database Connection
# Write a Python code snippet that demonstrates establishing a connection to a PostgreSQL database and executing a query to retrieve data.
# Example:
# (See code for usage)
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="password",
    database="example"
)

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM users")

# Fetch all rows
rows = cursor.fetchall()

# Print the data
for row in rows:
    print(row)

# Close the cursor and the connection
cursor.close()
conn.close() 
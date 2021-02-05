import sqlite3

# Basic functionality for SQLite databases
def open_database(filename):
    connection = sqlite3.connect( filename )
    connection.row_factory = sqlite3.Row
    return connection

def read_database(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    result = [ dict(row) for row in cursor.fetchall() ]
    return result

def write_database(connection, sql):
    cursor = connection.cursor()
    rows_affected = cursor.execute(sql).rowcount
    connection.commit()
    return rows_affected

def close_database(connection):
    connection.close()

filename = "test.db"

CONNECTION = open_database(filename)
SQL_COMMAND = 'SELECT * FROM People WHERE age>=40'

print(read_database(CONNECTION, SQL_COMMAND))
print(type(read_database(CONNECTION, SQL_COMMAND)))   # the queries is in a list

close_database(CONNECTION)

option = input("What CRUD operation would you like to do?")

if option == "C": #create

elif option == "R": #read

elif option == "U": #update

elif option == "D": #delete

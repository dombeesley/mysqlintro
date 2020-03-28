import datetime
import pymysql


# Connect to the database
connection = pymysql.connect(host='localhost',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                          Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) if the
        # table already exists

        
finally:
    # Close the connection, regardless of whether above was successful
    connection.close()

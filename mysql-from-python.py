import datetime
import pymysql


# Connect to the database
connection = pymysql.connect(host='localhost',
                             db='Chinook')

try: 
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'bob';")
        connection.commit()


finally:
    # Close the connection, regardless of whether above was successful
    connection.close()

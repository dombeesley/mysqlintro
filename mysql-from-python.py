import datetime
import pymysql


# Connect to the database
connection = pymysql.connect(host='localhost',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        rows = cursor.execute("delete from Friends where name = 'Bob';")
        connection.commit()


finally:
    # Close the connection, regardless of whether above was successful
    connection.close()

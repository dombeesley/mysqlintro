import datetime
import pymysql


# Connect to the database
connection = pymysql.connect(host='localhost',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        rows = [("bob", 21, "1990-02-06 23:04:56"),
                ("jim", 56, "1955-05-09 13:12:45"),
                ("fred", 100, "1911-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
        connection.commit()


finally:
    # Close the connection, regardless of whether above was successful
    connection.close()

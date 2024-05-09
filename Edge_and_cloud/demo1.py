import mysql.connector

cnx = mysql.connector.connect(user='shivam', password='shivam12',
                              host='localhost',
                              database='student')
cnx.close()
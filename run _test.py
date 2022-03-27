
import mysql.connector
from mysql.connector import Error
from sympy import Q
import pandas as pd
import numpy as np
try:
    connection = mysql.connector.connect(host='132.66.207.29',
                                         database='covdb_dev',
                                         user='admin',
                                         password='secretpass1',
                                         port='9100')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        ## defining the Query to use
        SQL_Query = "SELECT sequence FROM sequence limit 10"
        cursor.execute(SQL_Query)
        data = cursor.fetchall()
        df = pd.DataFrame(data,columns=['sequence'])
        print(df)
        df.to_csv('sequnecs.txt', sep='\t', index=False)
        #   print(pair)
        #print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
    exit()
    
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


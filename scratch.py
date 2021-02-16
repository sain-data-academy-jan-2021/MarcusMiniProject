import pymysql
import os
import tabulate
from dotenv import load_dotenv

products = []
couriers = []

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")
connection = pymysql.connect(host, user, password, database)

# def ReadFromDatabase(table):
#     cursor = connection.cursor()
#     cursor.execute(f"SELECT * FROM {table}")
#     rows = cursor.fetchall()
#     column_names = [i[0] for i in cursor.description]
#     result = []
#     for row in rows:
#         outerdict = {}
#         j = 0
#         for x in row:
#             innderdict = {column_names[j]: x}
#             j += 1
#             outerdict = {**outerdict, **innderdict} 
#         result.append(outerdict)
#     cursor.close()
#     connection.commit()
#     return result

def read_from_database(table):
    result = []
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table}')
    rows = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]
    for row in rows:
        outerdict = {}
        j = 0
        for x in row:
            outerdict[column_names[j]] = x
            j += 1
        result.append(outerdict)
    cursor.close()
    return result 

def PrintList(list): #prints whatever list is given
    #changing the tables headers based on which list id given
    if list == products:
        header = ["Product ID", "Product Name", "Category", "Price"]
    elif list == couriers:
        header = ["Courier ID", "Courier Name", "Vehicle"]
    #uses "tabulate" to draw a pretty table
    rows =  [x.values() for x in list]
    print(tabulate.tabulate(rows, header, tablefmt='rst'))
    
def UpdateProductDB(table_string): #product only
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table_string}')
    column_names = [i[0] for i in cursor.description]
    print(column_names)
    cursor.close()
    cursor = connection.cursor()
    index = int(input("What ID would you like to update: "))
    column = input("What column would youlike to update: ")
    update = input("What would you like to change it to: ")
    cursor.execute(f"UPDATE {table_string} SET {column} = '{update}' WHERE {column_names[0]} = '{index}'")
    cursor.close()
    connection.commit()
    print ( "Data entered successfully." )
    
def DeleteDB(table_string):
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table_string}')
    column_names = [i[0] for i in cursor.description]
    cursor.close()
    cursor = connection.cursor()
    index = int(input("What ID would you like to delete: "))
    cursor.execute(f"DELETE FROM {table_string} WHERE {column_names[0]} = '{index}'")
    cursor.close()
    connection.commit()
    print ( "Data entered successfully." )

products = read_from_database("products")
PrintList(products)
DeleteDB("products")

import os
import pymysql
import tabulate
from dotenv import load_dotenv
from modules.draw_func import PrintTable

def Connect2DB():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    return pymysql.connect(host, user, password, database)

def DBSelect(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    return cursor.fetchall(), cursor.description

def DBEdit(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    connection.commit()

def GetOrderID(connection):
    current_Orders= [id[0] for id in DBSelect(connection, "SELECT order_id FROM orders")[0]] # 0 because DBSelect returns 2 values
    PrintTable(connection, "orders")
    while True:
        id = input("Please select an an order id to view its basketPlease select an courier ID: ")
        if int(id) in current_Orders:
            break
        elif int(id) not in current_Orders:
            print("That order doesn't exist")
            continue
    return id
    
def PrepareJoinTable(connection):
    result = []
    order_id = GetOrderID(connection)
    rows, column = DBSelect(connection, f"SELECT b.order_id, p.product_name FROM basket b JOIN products p ON b.product_id = p.product_id WHERE b.order_id = {order_id}")
    column_names = [i[0] for i in column]
    for row in rows:
        outerdict = {}
        j = 0
        for x in row:
            outerdict[column_names[j]] = x
            j += 1
        result.append(outerdict)
    return result

def PrintJoinTable(connection):
    list = PrepareJoinTable(connection)
    header = ["Order ID", "Product Name"]
    rows =  [x.values() for x in list]
    print(tabulate.tabulate(rows, header, tablefmt='rst', stralign = "center", numalign = "center"))

connection = Connect2DB()
PrintJoinTable(connection)
connection.close()
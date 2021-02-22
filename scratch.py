import os
import pymysql
import tabulate
from modules.draw_func import *
from modules.utils import *
from dotenv import load_dotenv

def Connect2DB():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    return pymysql.connect(host, user, password, database)

# ----- Menus layout -----
def DrawMainMenu():
    DrawTitle("Buy & Co.")
    print("""+| 1) Product Menu         |+ 
+| 2) Courier Menu         |+
+| 3) Order Menu           |+
+| 4) Testing              |+""")
    DrawTitle("Exit")

def DrawOrderMenu():
    DrawTitle("Order Menu")
    print("""+| 1) Create New Order     |+ 
+| 2) Full Orders List     |+
+| 3) Update Order Status  |+
+| 4) Delete an order      |+
+| 6) Main Menu            |+""")
    DrawTitle("Exit")
    
def MainMenuChoice():
    while True:
        DrawMainMenu()
        menu_selection = (input("Please select a menu from above: ")).lower()
        print(f"this is your menu selection {menu_selection}")
        if menu_selection in ["1", "2", "3", "4", "exit"]:
                break
        else:
            Clear()
            print("please select a number between 1 and 4, or exit to quit")
    return menu_selection

def OrderMenuChoice():
    while True:
        DrawOrderMenu()
        menu_selection = (input("Please select a menu from above: ")).lower()
        if menu_selection in ["1", "2", "3", "4", "6", "exit"]:
            break
        else:
            Clear()
            print("please select a number between 1 and 4, or exit to quit")
    return menu_selection

def MainMenu():
    while True:
        choice = MainMenuChoice()
        if choice == "1":
            print("Products Menu")
        elif choice == "2":
            print("Couriers Menu") 
        elif choice == "3":
            Clear()
            OrderMenu()
        elif choice == "4":
            print("Testing Menu")
        elif choice == "exit":
            print("Exit")

def OrderMenu():
    connection = Connect2DB()
    while True:
        choice = OrderMenuChoice()
        if choice == "1": #creates a new order
            NewOrder(connection)
        elif choice == "2": # prints orders table
            PrintTable(connection, "orders")
        elif choice == "3":
            print("Update Menu")
        elif choice == "4":
            DeleteOrder(connection) # deletes an order
        elif choice == "exit":
            print("Exit")
    connection.close()

def GetCourierID(connection):
    current_couriers_id, = [id[0] for id in DBSelect(connection, "SELECT courier_id FROM couriers")]
    ViewCourier(connection)
    while True:
        id = input("Please select an courier ID: ")
        if int(id) in current_couriers_id:
            break
        elif int(id) not in current_couriers_id:
            print("That Courier doesn't exist")
            continue
    return id
    
# ----- product functions -----
def ViewProducts(connection):
    for product in DBSelect(connection, "SELECT * FROM products"):
        print(product)
        
# ----- Courier functions -----
def ViewCourier(connection):
    for courier in DBSelect(connection, "SELECT * FROM couriers"):
        print(courier)

# ----- order functions -----
def ViewOrders(connection):
    for order in DBSelect(connection, "SELECT * FROM orders"):
        print(order)
        
def NewOrder(connection):
    customer_name = input("Please enter the new customer name ").lower()
    courier_id = GetCourierID(connection)
    DBEdit(connection, f"INSERT INTO orders (customer_name, courier_id, status) VALUES ('{customer_name}', '{courier_id}', 'accepted')")
    order_id = DBSelect(connection, "SELECT MAX(order_id) FROM orders")[0][0]
    ViewProducts(connection)
    shopping_basket = input("enter the IDs: ")
    basket_list = shopping_basket.split(", ")
    for i in basket_list:
        DBEdit(connection, f"INSERT INTO basket (order_id, product_id) VALUES ({order_id}, {i})")

def DeleteOrder(connection):
    current_order_id = [id[0] for id in DBSelect(connection, "SELECT order_id FROM orders")]
    while True:
        ViewOrders(connection)
        delete_id = int(input("please enter the ID of the order to be deleted: "))
        if int(delete_id) in current_order_id:
            DBEdit(connection, f"DELETE FROM basket WHERE order_id = {delete_id}")
            DBEdit(connection, f"DELETE FROM orders WHERE order_id = {delete_id}")
            break
        else:
            print("Please Select a valid ID")

        
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

def PrintTable(connection, table,):
    result = []
    rows,column = DBSelect(connection, f"SELECT * FROM {table}")
    column_names = [i[0] for i in column]
    for row in rows:
        outerdict = {}
        j = 0
        for x in row:
            outerdict[column_names[j]] = x
            j += 1
        result.append(outerdict)
    print(result)
    return result
        
# ----- App -----
MainMenu()



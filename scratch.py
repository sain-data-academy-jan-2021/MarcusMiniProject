<<<<<<< HEAD
import csv
=======
>>>>>>> dbea5c5fc8233a346e6454db11378c0ed09dbd6c
import os
import pymysql
import tabulate
<<<<<<< HEAD
import pymysql
from modules.draw_func import DrawTitle
from modules.utils import *
from modules.data_persistance import *
from dotenv import load_dotenv

orders = []
products = []
couriers = []

# ------------ Global Functions ------------

def PrintList(list, list_string): #prints whatever list is given
    list = ReadFromDatabase(list_string)
    #changing the tables headers based on which list id given
    if list == orders:
        header = ["Customer ID", "Customer Name", "Order", "Status"]
    elif list == products:
        header = ["Product ID", "Product Name", "Category", "Price"]
    elif list == couriers:
        header = ["courier ID", "Courier Name", "Vehicle"]
    #uses "tabulate" to draw a pretty table
    rows =  [x.values() for x in list]
    print(tabulate.tabulate(rows, header, tablefmt='rst'))
    
# ------------ Menu Navigation Functions ------------
def MainMenu():
    DrawTitle("Buy & Co.")
    print("""+| 1) Product Menu         |+ 
+| 2) Courier Menu         |+
+| 3) Order Menu           |+
+| 4) Testing              |+""")
    DrawTitle("Exit")

def ProductMenu():
    DrawTitle("Product Menu")
    print("""+| 1) Full product list    |+ 
+| 2) Add a new product    |+
+| 3) Remove a product     |+
+| 4) Update a product     |+
+| 6) Main Menu            |+""")
    DrawTitle("Exit")
    
def CourierMenu():
    DrawTitle("Courier Menu")
    print("""+| 1) Full Courier List    |+ 
+| 6) Main Menu            |+""")
    DrawTitle("Exit")
    
def OrderMenu():
    DrawTitle("Order Menu")
    print("""+| 1) Create New Order     |+ 
+| 2) Full Orders List     |+
+| 3) Update Order Status  |+
+| 6) Main Menu            |+""")
    DrawTitle("Exit")

def Goodbye():
    Clear()
    print("""
    +|=========================|+
    +|     Have a nice day     |+
    +|         O     O         |+
    +|            -            |+
    +|         -_____-         |+
    +|=========================|+
    """)
    connection.close
    exit()
    
def MenuStart(Menu):
    Menu
    Option = input("Please select an option").lower()
    return Option

def Return():
    exit = str(input("Would you like to return to the previous menu?")).lower()
    if exit in ["y", "yes"]:
        Clear()
        return
    elif exit in ["n", "no"]:
        Goodbye()

# ------------ Product Functions ------------

# ------------ Courier Functions ------------

# ------------ Order Functions ------------
def NewDBOrder():
    # --- creating the first order part
    cursor = connection.cursor()
    customer_name = input("Please enter the new customer name ").lower()
    PrintList(couriers, "couriers")
    courier_id = input("Please select the ID of the courier ")
    cursor.execute(f"INSERT INTO orders (customer_name, courier_id, status) VALUES ('{customer_name}', '{courier_id}', 'accepted')")
    id = cursor.lastrowid #gets the last id entered
    Clear()
    PrintList(products, "products")
    shopping_basket = input("enter the IDs: ")# "1, 3 4"
    basket_list = shopping_basket.split(", ")# [1, 3,4]
=======
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
>>>>>>> dbea5c5fc8233a346e6454db11378c0ed09dbd6c
    for i in basket_list:
        DBEdit(connection, f"INSERT INTO basket (order_id, product_id) VALUES ({order_id}, {i})")

<<<<<<< HEAD
# --------------- Main App --------------------
if __name__ == "__main__": # only runs if app.py is ran directly
    # --- reads in from the  tables ---
    products = ReadFromDatabase("products")
    couriers = ReadFromDatabase("couriers")
=======
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

>>>>>>> dbea5c5fc8233a346e6454db11378c0ed09dbd6c

    while True:
        Clear()
        option = MenuStart(MainMenu()) # starts the function by calling the first menu
    # --------- Product Menu ------------
        if option == "1":
            while True:
                Clear()
                option = MenuStart(ProductMenu())
                if option == "1": #Product List
                    Clear()
                    PrintList(products,"products")
                    Return()
                elif option == "2": #Add a Product
                    Clear()
                    PrintList(products, "products")
                    NewDBProduct()
                    Return()
                elif option == "3": #Remove a product
                    Clear()
                    PrintList(products, "products")
                    DeleteDB("products")
                    Return()
                elif option == "4": #Remove a product
                    Clear()
                    PrintList(products, "products")
                    UpdateDB("products")
                    Return()    
                    
                elif option == "6": #Return to Main Menu
                    break    
                elif option == "exit": #Exit
                    Goodbye()
                else:
                    print("Try again:")
                    input("Please enter a valid option: ")
                    Clear()
                    option = MenuStart(ProductMenu())
    # -------- Courier Menu ---------
        elif option == "2": #Courier Menu
            while True:
                Clear()
                option = MenuStart(CourierMenu())
                if option == "1": #Courier List
                    Clear()
                    PrintList(couriers, "couriers")
                    Return()
                elif option == "6": #Main Menu
                    break
                elif option == "exit": #Exit
                    Goodbye()
                    exit()
                else:
                    print("Try again")
                    input("Please enter a valid option")
                    Clear()
                    option = MenuStart(CourierMenu())
        elif option == "3": #Order Menu
    #       |------ order menu
            while True:
                Clear()
                option = MenuStart(OrderMenu())
                if option == "1": #create new order
                    Clear()
                    NewDBOrder()
                    Return()
                elif option == "2":
                    Clear()
                    Return()
                elif option == "3":
                    Clear()
                    Return()
                elif option == "6": #Main Menu
                    break
                elif option == "exit": #Exit
                    Goodbye()
                    exit()
                else:
                    print("Try again")
                    input("Please enter a valid option")
                    Clear()
                    option = MenuStart(OrderMenu())
    #   |----- Main menu --------------
        elif option == "4": #test
            print(couriers)
            # NewDBProduct()#test new function
            Return()
            
        elif option == "exit": #Exit
            Goodbye()
            exit()
        else:
            print("Try again")
            input("Please enter a valid option")
            Clear()
            option = MenuStart(MainMenu())
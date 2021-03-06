import os
from modules.draw_func import DrawLine, DrawTitle, PrintTable
from modules.utils import Clear
from modules.data_persistance import Connect2DB
from modules.product_functions import NewDBProduct
from modules.order_functions import NewOrder, DeleteOrder, PrintJoinTable
from modules.courier_functions import NewDBCourier
from modules.database_functions import DeleteFromDB

# ---------------------------- Product Menu -------------------------- 
def DrawMainMenu():
    DrawTitle("Buy & Co.")
    print("""+| 1) Product Menu         |+ 
+| 2) Courier Menu         |+
+| 3) Order Menu           |+
+| 4) Testing              |+""")
    DrawTitle("Exit")

def MainMenuChoice():
    while True:
        DrawMainMenu()
        menu_selection = (input("Please select a menu from above: ")).lower()
        if menu_selection in ["1", "2", "3", "4", "exit"]:
                break
        else:
            Clear()
            print("please select a number between 1 and 4, or exit to quit")
    return menu_selection

def MainMenu():
    Clear()
    while True:
        choice = MainMenuChoice()
        if choice == "1":
            Clear()
            ProductMenu()
        elif choice == "2":
            Clear()
            CourierMenu()
        elif choice == "3": # orders menu
            Clear()
            OrderMenu()
        elif choice == "4":
            print("Testing Menu") #this is for testing single test functions
        elif choice == "exit":
            Goodbye()

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
    exit()

def Return():
    exit = str(input("Would you like to return to the previous menu?")).lower()
    if exit in ["y", "yes"]:
        Clear()
        return
    elif exit in ["n", "no"]:
        Goodbye()
# ---------------------------- Product Menu --------------------------           
def DrawProductMenu():
    DrawTitle("Order Menu")
    print("""+| 1) Create New Product   |+ 
+| 2) Full Products List   |+
+| 3) Delete a product     |+
+| 6) Main Menu            |+""")
    DrawTitle("Exit")
    
def ProductMenuChoice():
    while True:
        DrawProductMenu()
        menu_selection = (input("Please select a menu from above: ")).lower()
        if menu_selection in ["1", "2", "3", "6", "exit"]:
            break
        else:
            Clear()
            print("please select a number between 1 and 3, or exit to quit")
    return menu_selection

def ProductMenu():
    connection = Connect2DB()
    while True:
        choice = ProductMenuChoice()
        if choice == "1": #creates a new product
            Clear()
            NewDBProduct(connection)
            Return()
        elif choice == "2": # prints products table
            Clear()
            PrintTable(connection, "products")
            Return()
        elif choice == "3": # deletes a product
            Clear()
            DeleteFromDB(connection, "products")
            Return()
        elif choice == "6": # returns to main menu
            Clear()
            MainMenu()
        elif choice == "exit":
            Goodbye()
    connection.close()

# ---------------------------- Courier Menu --------------------------    
def DrawCourierMenu():
    DrawTitle("Order Menu")
    print("""+| 1) Create New Courier   |+ 
+| 2) Full Couriers List   |+
+| 3) Delete an Courier    |+
+| 6) Main Menu            |+""")
    DrawTitle("Exit")
    
def CourierMenuChoice():
    while True:
        DrawCourierMenu()
        menu_selection = (input("Please select a menu from above: ")).lower()
        if menu_selection in ["1", "2", "3", "6", "exit"]:
            break
        else:
            Clear()
            print("please select a number between 1 and 3, or exit to quit")
    return menu_selection

def CourierMenu():
    connection = Connect2DB()
    while True:
        choice = CourierMenuChoice()
        if choice == "1": #creates a new courier
            Clear()
            NewDBCourier(connection)
            Return()
        elif choice == "2": # prints couriers table
            Clear()
            PrintTable(connection, "couriers")
            Return()
        elif choice == "3": #deletes a product
            Clear()
            DeleteFromDB(connection, "couriers")
            Return()
        elif choice == "6":
            Clear()
            MainMenu()
        elif choice == "exit":
            Goodbye()
    connection.close()
# ---------------------------- Order Menu --------------------------   
def DrawOrderMenu():
    DrawTitle("Order Menu")
    print("""+| 1) Create New Order     |+ 
+| 2) Full Orders List     |+
+| 3) Delete an order      |+
+| 4) Print Basket Report  |+
+| 6) Main Menu            |+""")
    DrawTitle("Exit")
    
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

def OrderMenu():
    connection = Connect2DB()
    while True:
        choice = OrderMenuChoice()
        if choice == "1": #creates a new order
            Clear()
            NewOrder(connection)
            Return()
        elif choice == "2": # prints orders table
            Clear()
            PrintTable(connection, "orders")
            Return()
        elif choice == "3": # deletes an order
            Clear()
            DeleteOrder(connection) 
            Return()
        elif choice == "4": # deletes an order
            Clear()
            PrintJoinTable(connection)
            Return()
        elif choice == "6":
            MainMenu()
        elif choice == "exit":
            Goodbye()
    connection.close()
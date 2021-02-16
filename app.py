import csv
import os
import tabulate
import pymysql
from modules.draw_func import DrawTitle
from modules.utils import *
from modules.data_persistance import *
from dotenv import load_dotenv

orders = []
products = []
couriers = []

# ------------ Global Functions ------------

def PrintList(list): #prints whatever list is given
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


if __name__ == "__main__": # only runs if app.py is ran directly
    # --- reads in from the 3 csv files ---
    orders = FromCSV("orders", orders)
    products = ReadFromDatabase("products")
    couriers = ReadFromDatabase("couriers")

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
                    products = ReadFromDatabase("products") #gets the most up to date version
                    PrintList(products)
                    Return()
                elif option == "2": #Add a Product
                    Clear()
                    products = ReadFromDatabase("products") #gets the most up to date version
                    PrintList(products)
                    NewDBProduct()
                    Return()
                elif option == "3": #Remove a product
                    Clear()
                    PrintList(products)
                    DeleteDB("products")
                    Return()
                elif option == "4": #Remove a product
                    Clear()
                    PrintList(products)
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
                    PrintList(couriers)
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
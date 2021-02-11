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

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

connection = pymysql.connect(
  host,
  user,
  password,
  database
)
# ------------ Global Functions ------------

def ReadFromDatabase(table):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    field_names = [i[0] for i in cursor.description]
    for row in rows:
        db_dict = {field_names[0]: row[0], field_names[1]: row[1], field_names[2]: row[2], field_names[3]: row[3]}
        table.append(db_dict)
    cursor.close()
    connection.commit()
    return table

    
def SortDict(list, key): # sorts a given list, in order of a key, then prints it
    newlist = sorted(list, key=lambda k: k[key])
    if list == orders:
        header = ["Customer ID", "Customer Name", "Order", "Status"]
    elif list == products:
        header = ["Product ID", "Product Name", "Category", "Price"]
    elif list == couriers:
        header = ["courier ID", "Courier Name", "Vehicle"]
    rows =  [x.values() for x in newlist]
    print(tabulate.tabulate(rows, header, tablefmt='rst'))

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

def FindIndex(lst, key, value): # finds a value
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return "Not in list"

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
        return True
    elif exit in ["n", "no"]:
        Goodbye()

# ------------ Product Functions ------------
def NewDBProduct():
    cursor = connection.cursor()
    p_product_name = input("Please enter the new products name: ").lower()
    p_category = input("What category is the new product: ").lower()
    p_price = input("How much is it: ")
    cursor.execute(f"INSERT INTO products (product_name, category, price) VALUES ('{p_product_name}', '{p_category}', {p_price})")
    cursor.close()
    connection.commit()
    print ( "Data entered successfully." )

def RemoveProduct(): # removes a product via its product ID
    product2delete = input("Please enter a product id to delete: ")
    for i in range(len(products)): 
        if products[i]["product_id"] == product2delete:
            del products[i]
            break
        
# ------------ Courier Functions ------------

# ------------ Order Functions ------------
def UpdateStatus(): #updates the order status
    PrintList(orders)
    order_id = (input("Enter the customer's ID: "))
    for info in orders:
        if info["customer_id"] == order_id:
            info["status"] = "Out for delivery"

def NewBasket():
    basket = []
    PrintList(products)
    name = input("Please select products from the menu: ").lower()
    newproductlist = name.split(", ") #allows multiple inputs
    for item in newproductlist:
        i = (FindIndex(products,"product_name", item))
        basket.append(i)
        print(i)
    return basket

def NewOrder():
    id = Last_Num(orders)
    name = input("Enter the customer name: ").lower()
    basket = NewBasket()
    status = "Accepted" #default vaalue for everynew order
    order = {"customer_id" : id, "customer_name" : name, "order" : basket, "status" : status}
    orders.append(order)
    return orders

if __name__ == "__main__": # only runs if app.py is ran directly
    # --- reads in from the 3 csv files ---
    orders = FromCSV("orders", orders)
    # products = FromCSV("products", products)
    products = ReadFromDatabase("products")
    couriers = FromCSV("couriers", couriers)
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
                    products = ReadFromDatabase("products") #gets the most up to date version from the database
                    PrintList(products)
                    Return()
                elif option == "2": #Add a Product
                    Clear()
                    NewDBProduct()
                    Return()
                elif option == "3": #Remove a product
                    Clear()
                    RemoveProduct()
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
                    NewOrder()
                    Return()
                elif option == "2":
                    Clear()
                    PrintList(orders)
                    Return()
                elif option == "3":
                    Clear()
                    PrintList(orders)
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
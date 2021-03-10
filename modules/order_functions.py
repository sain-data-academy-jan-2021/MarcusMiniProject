import tabulate
from modules.courier_functions import GetCourierID
from modules.data_persistance import DBEdit, DBSelect
from modules.draw_func import PrintTable

def NewOrder(connection):
    customer_name = input("Please enter the new customer name ").lower()
    courier_id = GetCourierID(connection)
    DBEdit(connection, f"INSERT INTO orders (customer_name, courier_id, status) VALUES ('{customer_name}', '{courier_id}', 'accepted')")
    order_id = DBSelect(connection, "SELECT MAX(order_id) FROM orders")[0][0][0]
    PrintTable(connection, "products")
    shopping_basket = input("enter the IDs: ")
    basket_list = shopping_basket.split(", ")
    for i in basket_list:
        DBEdit(connection, f"INSERT INTO basket (order_id, product_id) VALUES ({order_id}, {i})")

def DeleteOrder(connection): #deletes an orderfrom the basket first toavoid conflict
    current_order_id = [id[0] for id in DBSelect(connection, "SELECT order_id FROM orders")[0]]
    while True:
        PrintTable(connection, "orders")
        delete_id = int(input("please enter the ID of the order to be deleted: "))
        if int(delete_id) in current_order_id:
            DBEdit(connection, f"DELETE FROM basket WHERE order_id = {delete_id}")
            DBEdit(connection, f"DELETE FROM orders WHERE order_id = {delete_id}")
            break
        else:
            print("Please Select a valid ID")

def GetOrderID(connection):
    current_Orders= [id[0] for id in DBSelect(connection, "SELECT order_id FROM orders")[0]] # 0 because DBSelect returns 2 values
    PrintTable(connection, "orders")
    while True:
        id = input("Please select an an order id to view its basket: ")
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
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

def DeleteOrder(connection):
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
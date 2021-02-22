from modules.data_persistance import DBEdit, DBSelect
from modules.draw_func import PrintTable

def NewDBProduct(connection):
    name = input("Please enter the new products name: ").lower()
    category = input("What category is the new product: ").lower()
    price = input("How much is it: ")
    DBEdit(connection, f"INSERT INTO products (product_name, category, price) VALUES ('{name}', '{category}', {price})")
    print ("Data entered successfully.")
    
def DeleteProduct(connection):
    current_product_id = [id[0] for id in DBSelect(connection, "SELECT product_id FROM products")[0]]
    while True:
        PrintTable(connection, "products")
        delete_id = int(input("please enter the ID of the product to be deleted: "))
        if int(delete_id) in current_product_id:
            DBEdit(connection, f"DELETE FROM products WHERE product_id = {delete_id}")
        else:
            print("Please Select a valid ID")
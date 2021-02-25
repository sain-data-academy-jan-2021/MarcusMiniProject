from modules.data_persistance import DBEdit, DBSelect
from modules.draw_func import PrintTable

def NewDBProduct(connection):
    name = input("Please enter the new products name: ").lower()
    category = input("What category is the new product: ").lower()
    price = input("How much is it: ")
    DBEdit(connection, f"INSERT INTO products (product_name, category, price) VALUES ('{name}', '{category}', {price})")
    print ("Data entered successfully.")
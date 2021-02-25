from modules.data_persistance import DBEdit, DBSelect
from modules.draw_func import PrintTable
from modules.utils import Clear
import pymysql

def DeleteFromDB(connection, table):
    current_ids = [id[0] for id in DBSelect(connection, f"SELECT * FROM {table}")[0]]
    column_names = [id[0] for id in DBSelect(connection, f"SELECT * FROM {table}")[1]]
    while True:
        PrintTable(connection, table)
        delete_id = int(input("please enter the ID to be deleted (0 to cancel): "))
        Clear()
        if int(delete_id) == 0:
            break
        if int(delete_id) in current_ids:
            try:
                DBEdit(connection, f"DELETE FROM {table} WHERE {column_names[0]} = {delete_id}")
                print("That ID has been deleted")
                break
            except pymysql.err.IntegrityError: #error when trying to delete an id as a foreign key in another table
                print("The product is already in an order")
        else:
            print("Please Select a valid ID")
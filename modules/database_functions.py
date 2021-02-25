from modules.data_persistance import DBEdit, DBSelect
from modules.draw_func import PrintTable

def DeleteFromDB(connection, table):
    current_ids = [id[0] for id in DBSelect(connection, f"SELECT * FROM {table}")[0]]
    column_names = [id[0] for id in DBSelect(connection, f"SELECT * FROM {table}")[1]]
    while True:
        PrintTable(connection, table)
        delete_id = int(input("please enter the ID to be deleted: "))
        if int(delete_id) in current_ids:
            DBEdit(connection, f"DELETE FROM {table} WHERE {column_names[0]} = {delete_id}")
            break
        else:
            print("Please Select a valid ID")
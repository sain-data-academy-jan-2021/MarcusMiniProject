from modules.data_persistance import DBSelect, DBEdit
from modules.draw_func import PrintTable

def GetCourierID(connection):
    current_couriers_id = [id[0] for id in DBSelect(connection, "SELECT courier_id FROM couriers")[0]] # 0 because DBSelect returns 2 values
    PrintTable(connection, "couriers")
    while True:
        id = input("Please select an courier ID: ")
        if int(id) in current_couriers_id:
            break
        elif int(id) not in current_couriers_id:
            print("That Courier doesn't exist")
            continue
    return id

def NewDBCourier(connection):
    name = input("Please enter the new courier's name: ").lower()
    vehicle = input("What vehicle are they driving: ").lower()
    DBEdit(connection, f"INSERT INTO couriers (courier_name, vehicle) VALUES ('{name}', '{vehicle}')")
    print ("Data entered successfully.")
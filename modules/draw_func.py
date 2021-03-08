import tabulate
from modules.data_persistance import DBSelect

def DrawLine():
    print("+|=========================|+")

def DrawTitle(title):
    item = title
    DrawLine()
    print("+| \033[1;33;40m" + item.capitalize() + ((24 - len(item)) * " ") + "\033[0;0;0m|+")
    DrawLine()

def PrintTable(connection, table):
    list = PreparePrintTable(connection, table)
    #changing the tables headers based on which list id given
    if table == "orders":
        header = ["Customer ID", "Customer Name", "Courier ID", "Status"]
    elif table == "products":
        header = ["Product ID", "Product Name", "Category", "Price"]
    elif table== "couriers":
        header = ["courier ID", "Courier Name", "Vehicle"]
    rows =  [x.values() for x in list]
    print(tabulate.tabulate(rows, header, tablefmt='rst', stralign = "center", numalign = "center"))

def PreparePrintTable(connection, table,):
    result = []
    rows, column = DBSelect(connection, f"SELECT * FROM {table}")
    column_names = [i[0] for i in column]
    for row in rows:
        outerdict = {}
        j = 0
        for x in row:
            outerdict[column_names[j]] = x
            j += 1
        result.append(outerdict)
    return result
import csv
import tabulate

test_list = [
    {"customer_id" : 1,
     "customer_name" : "Marcus",
     "status" : "Accepted"
     },
    {"customer_id" : 2,
     "customer_name" : "Steve",
     "status" : "Out for delivery"
     },
    {"customer_id" : 3,
     "customer_name" : "John",
     "status" : "Accepted"
     }]
products = []
newlist = []
couriers = []
orders =[]

def FromCSV(filename, list): #file name is the name of the CSV, list is what list csv is writing to
    try:
        with open(f"./csv/{filename}.csv", 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                list.append(row)
        return(list)
    except FileNotFoundError as err:
        print(f"Sorry the file '{filename}' could not be found: ", err)

def SortDict(list, key):
    newlist = sorted(list, key=lambda k: k[key])
    if list == orders:
        header = ["Customer ID", "Customer Name", "Order", "Status"]
    elif list == products:
        header = ["Product ID", "Product Name", "Category", "Price"]
    elif list == couriers:
        header = ["courier ID", "Courier Name", "Vehicle"]
    rows =  [x.values() for x in newlist]
    print(tabulate.tabulate(rows, header, tablefmt='rst'))    


FromCSV("products", products)
SortDict(products, "product_name")
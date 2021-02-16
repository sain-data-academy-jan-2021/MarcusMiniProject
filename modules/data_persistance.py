import os
import csv
import pymysql
from dotenv import load_dotenv

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

def ReadFromDatabase(table):
    result = []
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]
    for row in rows:
        outerdict = {}
        j = 0
        for x in row:
            outerdict[column_names[j]] = x
            j += 1
        result.append(outerdict)
    cursor.close()
    return result 

def NewDBProduct():
    cursor = connection.cursor()
    p_product_name = input("Please enter the new products name: ").lower()
    p_category = input("What category is the new product: ").lower()
    p_price = input("How much is it: ")
    cursor.execute(f"INSERT INTO products (product_name, category, price) VALUES ('{p_product_name}', '{p_category}', {p_price})")
    cursor.close()
    connection.commit()
    print ("Data entered successfully.")

def UpdateDB(table_string): #product only
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table_string}')
    column_names = [i[0] for i in cursor.description]
    print(column_names)
    cursor.close()
    cursor = connection.cursor()
    index = int(input("What ID would you like to update: "))
    column = input("What column would youlike to update: ")
    update = input("What would you like to change it to: ")
    cursor.execute(f"UPDATE {table_string} SET {column} = '{update}' WHERE {column_names[0]} = '{index}'")
    cursor.close()
    connection.commit()
    print ("Data updated successfully.")
    
def DeleteDB(table_string):
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table_string}')
    column_names = [i[0] for i in cursor.description]
    cursor.close()
    cursor = connection.cursor()
    index = int(input("What ID would you like to delete: "))
    cursor.execute(f"DELETE FROM {table_string} WHERE {column_names[0]} = '{index}'")
    cursor.close()
    connection.commit()
    print ("Data entered successfully.")
    
def FromCSV(filename, list): #file name is the name of the CSV, list is what list csv is writing to
    try:
        with open(f"./csv/{filename}.csv", 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                list.append(row)
        return(list)
    except FileNotFoundError as err:
        print(f"Sorry the file '{filename}' could not be found: ", err)
        


def ToCSV(filename, list): #file name is the name of the CSV, list is what list is being written to the csv
    keys = list[0].keys()
    with open(f"./csv/{filename}.csv", 'w', newline = '')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(list)
        

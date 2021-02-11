import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")
connection = pymysql.connect(host, user, password, database)

def NewDBProduct():
    cursor = connection.cursor()
    cursor.execute("INSERT INTO products (product_name, category, price) VALUES ('Lemonade', 'drink', 0.99)")
    cursor.close()
    connection.commit()
    print ( 'Data entered successfully.' )
    connection.close()

NewDBProduct()
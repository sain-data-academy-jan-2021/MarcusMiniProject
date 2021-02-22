import os
import pymysql
from dotenv import load_dotenv

def Connect2DB():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    return pymysql.connect(host, user, password, database)

def DBSelect(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    return cursor.fetchall(), cursor.description

def DBEdit(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    connection.commit()
#Simpl_connectionEx1.py
import mysql.connector as mc
try:
    obj = mc.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        use_pure=True,
    )
    print("My connected to MySQL database")
    cur = obj.cursor()
    cus="create database chandhana"
    cur.execute(cus)
    print("Data Base created in MySQL--verify")
except mc.DatabaseError as db:
    print("Problem in MySQL Database,db")


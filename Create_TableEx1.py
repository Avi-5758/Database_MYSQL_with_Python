#Create_TableEx1.py
#Create a Table in a DataBase.
import mysql.connector as mc
def create_Table():
    mydb=mc.connect(host="127.0.0.1",
                    user="root",
                    password="root",
                    database="test")
    cur=mydb.cursor()
    tc="create table student(sno int primary key,Emp_Name varchar(30) not null,Age int not null,Salary float not null)"
    cur.execute(tc)
    print("Table created successfully")

create_Table()
#tc = "create table Avi(sno int primary key, Emp_Name varchar(30) not null, Age int not null, Salary float not null default 0.0)"
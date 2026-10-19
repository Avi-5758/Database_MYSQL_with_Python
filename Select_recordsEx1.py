#Select_recordsEx1.py
#program for reading the Records from employee--fetchall()
import mysql.connector as mc
def select():
    mydc=mc.connect(host="127.0.0.1",
                    user="root",
                    password="root",
                    database="test")
    cur=mydc.cursor()
    tc="select * from chandhana"
    cur.execute(tc)
    print("*"*50)
    records=cur.fetchall()
    print(records)
    print("*"*50)
    print("-"*50)
    for record in records:
        for value in record:
            print("\t{}".format(value), end="\t")
        print()
    print("*"*50)
    print("-"*50)
select()
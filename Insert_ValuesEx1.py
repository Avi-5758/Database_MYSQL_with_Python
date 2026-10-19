# Insert_ValuesEx1.py
# Program to insert records into student table
import mysql.connector as mc

def insert_values():
    try:
        mydc = mc.connect(
            host="localhost",
            user="root",
            password="root",
            database="chandhana",
            port=3306
        )
        cur = mydc.cursor()

        while True:
            empno = int(input("Enter emp no: "))
            empname = input("Enter emp name: ")
            age = int(input("Enter age: "))
            salary = int(input("Enter salary: "))
            print("*" * 40)

            # Insert query matching your table schema
            sq = "INSERT INTO student VALUES (%s, %s, %s, %s)"
            cur.execute(sq, (empno, empname, age, salary))
            mydc.commit()

            if cur.rowcount > 0:
                print("{} Record Inserted successfully".format(cur.rowcount))
            else:
                print("Record Not Inserted")

            ch = input("\tWould you like to Insert Another Record? (yes/no): ")
            if ch.lower() == "no":
                print("THX for using the Program")
                break

        # Resource cleanup
        cur.close()
        mydc.close()

    except mc.Error as err:
        print("MySQL Error:", err)

insert_values()
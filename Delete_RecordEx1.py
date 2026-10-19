import mysql.connector as mc

def delete():
    mydb = mc.connect(
        host="localhost",
        user="root",
        password="root",
        database="chandhana"
    )
    cur = mydb.cursor()

    while True:
        empno = int(input("Enter emp no: "))
        cur.execute("delete from student where sno=%s", (empno,))
        mydb.commit()

        if cur.rowcount > 0:
            print("{} Record Deleted successfully".format(empno))
        else:
            print("Record Does not exist")

        ch = input("\tDo you want to Delete Another Record? (yes/no): ")
        if ch.lower() == "no":
            print("THX for using this program.")
            break



delete()
#Find_No_ColEx.py
#Program for display the Number of columns
import mysql.connector as mc
def findNo():
    mydc=mc.connect(host="localhost",
                    user="root",
                    password="root",
                    database="chandhana")
    cur=mydc.cursor()
    sq="select * from student "
    cur.execute(sq)
    print("*"*50)
    for colname in [colinfo[0] for colinfo  in cur.description]:
        print("\t{}".format(colname),end="\n")
    print()
    print("*"*50)


findNo()

#Create_TableEx2.py
# Create a table in a database.
import mysql.connector as mc
def create_table():
    mydc=mc.connect(host="127.0.0.1",
                    user="root",
                    password="root",
                    database="chandhana")
    cur=mydc.cursor()
    tc="Create table Employye( Roll_no int primary key, Std_Name varchar(30) not null,STD_No int not  null)"
    cur.execute(tc)
    mydc.commit()
    print("Successfully created table")

create_table()

"""# Create_TableEx2.py
import mysql.connector as mc

mydc = mc.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="chandhana",
    port=3306,
)
cur = mydc.cursor()

# Create table
tc = "CREATE TABLE IF NOT EXISTS student1 (Roll_no INT PRIMARY KEY, Std_Name VARCHAR(30) NOT NULL, STD_No INT NOT NULL)"
cur.execute(tc)
mydc.commit()

# Print exact MySQL server details Python is talking to
cur.execute(
    "SELECT CURRENT_USER(), DATABASE(), @@hostname, @@port, @@version;"
)
print("Python is connected to:", cur.fetchone())

# Check tables in this specific connection
cur.execute("SHOW TABLES;")
print("Tables in this connection:", cur.fetchall())

cur.close()
mydc.close()"""""
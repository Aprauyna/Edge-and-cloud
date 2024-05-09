import mysql.connector

cnx = mysql.connector.connect(
  user = "shivam",
  passwd = "shivam12",
  host = "localhost",
  database = "student"
)

cur = cnx.cursor()  
# sql = "insert into Employee(name, id, salary, Dept_id) values (%s, %s, %s, %s);"
# val = ("bhalu", 108, 150.4, 12)

try:  
    # dbs = cur.execute("create table Employee(name varchar(20) not null, id int(20) not null primary key, salary float not null, Dept_id int not null)")
    # dbs = cur.execute("create database cloud;")
    #  dbs = cur.execute("use cloud") 
    # cur.execute("insert into Employee values ('bhalu', 111, 141.2, 11);") 
    dbs = cur.execute("select * from Employee;") 
    # dbs = cur.execute("show tables;") 
    # dbs = cur.execute(sql, val) 
    # cnx.commit()  
except:  
    cnx.rollback()  

for x in cur:  
    print(x)  

print(cur.rowcount,"record inserted!")  

cnx.close()
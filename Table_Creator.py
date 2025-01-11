import mysql.connector as sql
import time
conn=sql.connect(host='localhost',user='root',password='AdminMahi')
if conn.is_connected():
      print("Sucessfully Connected")
try:
      c1=conn.cursor()
      cmd="Create database atm;"
      c1.execute(cmd)
      conn.commit()
      cmd="Use atm;"
      c1.execute(cmd)
      cmd="CREATE TABLE accounts(Acc_No int primary key,PIN INT(3),Name VARCHAR(20),Balance INT default(0), Access varchar(10));"
      c1.execute(cmd)
      conn.commit()
      print("Sucessfully Created")
      cmd="CREATE TABLE PDetails(Acc_No int,Name VARCHAR(20),Address varchar(100),Mobile_No bigint(10));"
      c1.execute(cmd)
      conn.commit()
      print("Sucessfully Created")
      cmd="CREATE TABLE Transactions(TransID int AUTO_INCREMENT Primary Key,Acc_No int,Time datetime,TransType varchar(20),Amount int);"
      c1.execute(cmd)
      conn.commit()
      print("Sucessfully Created")
      time.sleep(5)
except:
      print("Error Occurred")
      time.sleep(5)

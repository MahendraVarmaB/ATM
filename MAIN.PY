#Importing Libraries
import time
import mysql.connector as sql
import random

#Defining Repetitive Functions
def linebreak():
      print("================================================================================")
def endsession():
      l=False
      print("Thank you")
      print("PLEASE CLOSE THIS FILE BEFORE EXITING FOR SECURITY REASONS")
      print("Visit again!!!")
def timestamp():
      timeT = time.localtime() 
      return(time.strftime("%Y-%m-%d, %H:%M:%S"))

#Initialisations
count=0
l=True

# Establishing Connection with MySQL Server
conn=sql.connect(host="localhost",user="root",password="AdminMahi",database="ATM")
c1=conn.cursor()
linebreak()

 
# Main Code Blocks
print("                           WELCOME TO 'THE VAULT' ")
linebreak()

# Menu
print("1.Create Account")
print("2.Login")
print("3.Exit")

op=int(input("Enter your choice: "))
linebreak()
# Option 1
if op==1:
      c="y"
      while c=="y":
            acc=random.randint(1000000,9999999)
            cmd="select * from accounts where Acc_No={}".format(acc)
            c1.execute(cmd)
            d=c1.fetchall()
            data=c1.rowcount
            if data==1: # Checking if duplicates exists
                  continue
                  
            else: # Creating Acc with with unique Acc No.
                  print("Enter the following details very carefully")
                  name=input("Enter your name: ")
                  pin=int(input("Enter your PIN: "))
                  cmd="insert into accounts(Acc_No,PIN,Name,Access) values({},{},'{}','{}')".format(acc,pin,name,"Granted")
                  c1.execute(cmd)
                  conn.commit()
                  add=input("Enter your Address: ")
                  ph=input("Enter your Mobile Number: ")
                  cmd="insert into PDetails(Acc_No,Name,Address,Mobile_No) values({},'{}','{}',{})".format(acc,name,add,ph)
                  c1.execute(cmd)
                  conn.commit()
                  linebreak()
                  print("Account sucessfully created.")
                  print("Thank You for Opening an Account with us!!!")
                  linebreak()

                  print("Please save the following details \nAcc. No:",acc,"\nPIN:",pin)
                  # Minimum Balance requirement
                  print("Please note the minimum depoist is ₹1000")
                  deposit=int(input("Enter the money to be deposited :₹"))
                  linebreak()
                  if deposit<1000:
                        print("Please ensure to depoist the remaining ₹",1000-deposit," ASAP...")
                  cmd1="update accounts set Balance={} where Acc_No={}".format(deposit,acc)
                  cmd2="insert into Transactions(Acc_No,TransType,Time,Amount) values({},'{}','{}',{})".format(acc,"Deposit",timestamp(),deposit)
                  c1.execute(cmd1)
                  c1.execute(cmd2)
                  conn.commit()
                  print("Sucessfully Deposited")
                  linebreak()
                  endsession()
                  time.sleep(3)
                  exit()
# LOGIN
elif op==2:
      Y="Y"
      while Y=="Y":
            # User Authentication
            acc=int(input("Enter your account number: "))
            cmd="select Access from accounts where Acc_No={}".format(acc)
            c1.execute(cmd)
            a=c1.fetchone()
            
            data=c1.rowcount
            loopcheck=True
            while loopcheck==True:
                  if data==1:
                        if str(a[0])=="Granted":
                               while True:
                                    pin=int(input("Enter your PIN: "))
                                    linebreak()                                    
                                    cmd="select PIN from accounts where Acc_No={}".format(acc)
                                    c1.execute(cmd)
                                    a=c1.fetchone()
                                    d=list(a)
                                    if pin==d[0]:
                                          print("Correct PIN... Opening Menu")
                                          loopcheck=False
                                          # Main Menu
                                          while Y=="Y":
                                                linebreak()
                                                cmd="select Name from accounts where Acc_No={}".format(acc)
                                                c1.execute(cmd)
                                                a=c1.fetchone()
                                                print("Welcome",a[0],"!!!")
                                                linebreak()
                                                print("1.Deposit")
                                                print("2.Withdraw")
                                                print("3.Transfer Funds")
                                                print("4.Balance")
                                                print("5.Change PIN")
                                                print("6.Transaction History")
                                                print("7.Exit")
                                                linebreak()
                                                
                                                r=int(input("Enter your choice: "))
                                                linebreak()
                                                # Deposit
                                                if r==1:
                                                      amt=int(input("Enter the money to be deposited: ₹"))
                                                      linebreak()

                                                      cmd="update accounts set Balance=Balance + {} where Acc_No={}".format(amt,acc)
                                                      c1.execute(cmd)
                                                      conn.commit()
                                                      print("Sucessfully Deposited")

                                                      cmd="insert into Transactions(Acc_No,TransType,Time,Amount) values({},'{}','{}',{})".format(acc,"Deposit",timestamp(),amt)
                                                      c1.execute(cmd)
                                                      conn.commit()
                                                      
                                                      Y=input("Press Y to continue and any other key to exit : ").upper()
                                                      linebreak()
                  
                                                      if Y=="Y":
                                                            continue
                                                      else:
                                                            Y="N"
                                                            endsession()
                                                            time.sleep(3)
                                                            exit()
                                                # Withdraw           
                                                if r==2:
                                                      amt=int(input("Enter the money to withdraw: ₹"))
                                                      linebreak()

                                                      cmd="select Balance from accounts where Acc_No={}".format(acc)
                                                      c1.execute(cmd)
                                                      m=c1.fetchone()
                                                      if amt >m[0]:
                                                            print("Insufficient Funds... You have less than",amt)
                                                            print("Please Try Again")
                                                            linebreak()

                                                      else:
                                                            cmd="update accounts set balance=balance - {}  where Acc_No={}".format(amt,acc)
                                                            c1.execute(cmd)
                                                            conn.commit()

                                                            cmd="insert into Transactions(Acc_No,TransType,Time,Amount) values({},'{}','{}',{})".format(acc,"Withdrawl",timestamp(),amt)
                                                            c1.execute(cmd)
                                                            conn.commit()
                                                            
                                                            print("Sucessfully Withdrawn")
                                                            linebreak()
                                                      Y=input("Press Y to continue and any other key to exit: ").upper()
                                                      if Y=="Y":
                                                            continue
                                                      else:
                                                            Y="N"
                                                            endsession()
                                                            time.sleep(3)
                                                            exit()
                                                # Fund Transfer
                                                if r==3:
                                                      acct=int(input("Enter the account number to be transferred: "))
                                                      linebreak()

                                                      cmd="select * from accounts where Acc_No={}".format(acct)
                                                      c1.execute(cmd)
                                                      c1.fetchall()
                                                      data=c1.rowcount
                                                      if data==1:
                                                            print("Account Exists")
                                                            amt=int(input("Enter the money to be transferred: ₹"))
                                                            linebreak()

                                                            cmd="select Balance from accounts where Acc_No={}".format(acc)
                                                            c1.execute(cmd)
                                                            c=c1.fetchone()
                                                            if amt> c[0]:
                                                                  print("Insufficient Funds... You have less than ₹",amt)
                                                                  print("Please Try Again")
                                                                  linebreak()

                                                            else:
                                                                  cmd1="update accounts set balance=balance-{} where Acc_No={}".format(amt,acc)  
                                                                  cmd2="update accounts set balance=balance+{} where Acc_No={}".format(amt,acct)
                                                                  c1.execute(cmd1)
                                                                  c1.execute(cmd2)
                                                                  conn.commit()
                                                                  print("Sucessfully Transfered")
                                                                  
                                                                  cmd1="insert into Transactions(Acc_No,TransType,Time,Amount) values({},'{}','{}',{})".format(acc,"Outgoing Funds",timestamp(),amt)
                                                                  cmd2="insert into Transactions(Acc_No,TransType,Time,Amount) values({},'{}','{}',{})".format(acct,"Incoming Funds",timestamp(),amt)
                                                                  c1.execute(cmd1)
                                                                  c1.execute(cmd2)
                                                                  conn.commit()
                                                      
                                                                  linebreak()
                                                            Y=input("Press Y to continue and any other key to exit : ").upper()
                                                            if Y=="Y":
                                                                  continue
                                                            else:
                                                                  Y="N"
                                                                  endsession()
                                                                  time.sleep(3)
                                                                  exit()
                                                      else:
                                                            print("No such Account Exists !! Please Retry")
                                                            continue
                                                # Check Balance     
                                                if r==4:
                                                      cmd="select Balance from accounts where Acc_No={}".format(acc)
                                                      c1.execute(cmd)
                                                      k=c1.fetchone()
                                                      print("Balance in your account: ₹",int(k[0]))
                                                      linebreak()

                                                      Y=input("Press Y to continue and any other key to exit : ").upper()
                                                      if Y=="Y":
                                                            continue
                                                      else:
                                                            endsession()
                                                            time.sleep(3)
                                                            exit()
                                                # Change PIN            
                                                if r==5:
                                                      newpin=int(input("Enter new PIN: "))
                                                      ar="Update accounts set PIN={} where Acc_No={}".format(newpin,acc)
                                                      c1.execute(ar)
                                                      conn.commit()
                                                      print("Your PIN has been successfully changed")
                                                      linebreak()
                                                      Y=input("Press Y to continue and any other key to exit : ").upper()
                                                      if Y=="Y":
                                                            continue
                                                      else:
                                                            endsession()
                                                            time.sleep(3)
                                                            exit()
                                                # Transaction History            
                                                if r==6:
            
                                                      print("Date Format is YYYY,MM,DD,HH,MM,SS")
                                                      ar="select * from Transactions where Acc_No={}".format(acc)
                                                      c1.execute(ar)
                                                      data=c1.fetchall()
                                                      for row in data:
                                                            print(row)
                                                      Y=input("Press Y to continue and any other key to exit : ").upper()
                                                      if Y=="Y":
                                                            continue
                                                      else:
                                                            endsession()
                                                            time.sleep(3)
                                                            exit()
                                                # Exit      
                                                if r==7:
                                                      print("Exiting...")
                                                      endsession()
                                                      time.sleep(3)
                                                      exit()
                                          
                                    # Incorrect PIN loop     
                                    else:
                                          print("INCORRECT PIN")
                                          count+=1
                                          linebreak()
                                          if count !=5:
                                                print("You have",5-count,"trys left !!!")
                                          else:
                                                cmd="Update accounts set Access='{}' where Acc_No={}".format("Suspended",acc)
                                                c1.execute(cmd)
                                                conn.commit()
                                                print("Your Account has been Suspended")
                                                print("Please contact the Bank")
                                                linebreak()
                                                time.sleep(1)
                                                exit()
                        # Suspended Check                  
                        elif str(a[0])=="Suspended":
                              print("Your Account has been Suspended")
                              print("Please contact the Bank")
                              print("Exiting...")
                              time.sleep(2)
                              exit()
                  #Incorrect Acc No   
                  else:
                        print("Your Account does not exist... Please Try Again")
                        break

elif op==3:
      print("Exiting")
      print("Please close this file before exiting.")
      time.sleep(2)
      exit()

else:
      print ("Invalid Choice")
      print ("Exiting...")
      time.sleep(2)
      exit()
c1.close()

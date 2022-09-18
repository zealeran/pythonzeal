import datetime
import random
import mysql.connector
x=mysql.connector.connect(
    host="localhost",
    password="Eran@183",
    user="root",
    database="ATM",
 )
#y=x.cursor()
#y.execute("create database ATM")
#mycursor=x.cursor()
# val=(password,balance)
# sql="insert into atm_machine(password,balance)values(%s,%s)"
# mycursor.execute(sql,val)
# x.commit()
#y.execute("create table info(password int, account_number int,balance int,widhrawal_amount int,deposit_amount int)")
print("WELCOME TO ABC BANK")
print("Please insert your card")
print("1.WIDTHRAWAL""\t2.DEPOSIT""\t3.CHECKBALANCE"" \t4.EXIIT")
account_number=random.randint(1000,9999)
pin=1234
trial=3
balance=70000
while trial!=0:
    password=int(input("Please enter your pin:"))
    user=int(input("Enter your choice :"))
    y=x.cursor()
    val=(password,balance)
    sql="insert into mydb(password,balance)values(%s,%s)"
    y.execute(sql,val)
    x.commit()
    if password!=pin:
        trial-=1
    if password==pin:
            def WITHDRAWAL(widhrawal_amount):
                if widhrawal_amount<500:
                    print("only Rs.500 notes only available")
                if widhrawal_amount>500<=70000:
                    print("Please wait!your transaction is processing")
                    print(f"your withrawal amount is{widhrawal_amount}\n" f"your current balance is {balance}")
                if widhrawal_amount>70000:
                    print("insufficient money")
            def DEPOSIT(deposit_amount):
                print(f"your amount is {deposit_amount} is successfully deposited")
                print(f"your current balance is {balance} ")
            def CHECKBALANCE():
                z=datetime.datetime.now()
                print(z.strftime("%b %d, %Y   %I:%M:%S%p"))
                print(z.strftime("%A"))
                print(f"Account number is XXXXXXXX{account_number}")
                print(f"your account balance is:{balance}")
                y=x.cursor()
                val=[account_number,balance]
                sql="insert into mydb(account_number,balance)values(%s,%s)"
                y.execute(sql,val)
                x.commit()

                if receipt=="yes":
                    f=open("receipt.txt",'w')
                    f.write(z.strftime("%b %d, %Y   %I:%M:%S%p\n"))
                    f.write(z.strftime("%A\n"))
                    f.write(f"Account number is XXXXXXXX{account_number}\n")
                    f.write(f"your account balance is:{balance}\n")
                else:
                    print("Thank you")
            def EXIT():
                if out=="yes":
                    print("please collect your reaceipt")
                elif out=="no":
                    print("Thank you for visiting our atm")
                else:
                    print("Please remove and insert you card")
            if user==1:
                widhrawal_amount=int(input("please enter your amount:"))
                balance=balance-widhrawal_amount
                y=x.cursor()
                val=[widhrawal_amount]
                sql="insert into mydb(widhrawal_amount)values(%s)"
                y.execute(sql,val)
                x.commit()
                WITHDRAWAL(widhrawal_amount)
            elif user==2:
                deposit_amount=int(input("Enter your deposit amount:"))
                balance=balance+deposit_amount
                y=x.cursor()
                val=[deposit_amount]
                sql="insert into mydb(deposit_amount)values(%s)"
                y.execute(sql,val)
                x.commit()
                DEPOSIT(deposit_amount)
            elif user==3:
                receipt=str(input("do you want receipt(yes or no) :"))
                CHECKBALANCE()
            elif user==4:
                out=str(input("do you want to exit(yes or no) :")).lower().strip()
                EXIT()
            else:
                print("enter a valid choice number")
    else:
            print("invalid pin\nplease try again!")
            
            
    
    
            




    




    
    


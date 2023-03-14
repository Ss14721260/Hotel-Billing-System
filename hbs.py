
print(" don't use qutos for string values") 
import os
import platform
import mysql.connector
import pandas as pd
import datetime
global z
mydb=mysql.connector.connect(host='localhost',user='root', passwd='1234',database='hotel')
if mydb.is_connected():
    print('successfully connected to mysql database')
else:
    print('not connected to mysql database')
mycursor=mydb.cursor()


def registercust():
    L=[]
    custname=input("enter name:")
    L.append(custname)
    addr=input("enter address:")
    L.append(addr)
    indate=input("enter check in date:")
    L.append(indate)
    outdate=input("enter check out date:")
    L.append(outdate)
    cust=(L)
    sql="INSERT INTO custdata(custname,addr,indate,outdate)VALUES('{}','{}','{}','{}')".format(custname,addr,indate,outdate)
    mycursor.execute(sql)
    mydb.commit()
def roomtypeview():
    print("Do yoy want to see room type available : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select * from roomtype"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
def roomrent():
    print ("We have the following rooms for you:-")
    print ("1. type A---->rs 1000 PN\-")
    print ("2. type B---->rs 2000 PN\-")
    print ("3. type C---->rs 3000 PN\-")
    print ("4. type D---->rs 4000 PN\-")
    x=int(input("Enter Your Choice Please->"))
    custname=input('enter cust name=')
    n=int(input("For How Many Nights Did You Stay:"))
    if(x==1):
        print ("you have opted room type A")
        s=1000*n
    elif (x==2):
        print ("you have opted room type B")
        s=2000*n
    elif (x==3):
        print ("you have opted room type C")
        s=3000*n
    elif (x==4):
        print ("you have opted room type D")
        s=4000*n
    else:
        print ("please choose a room")
    print ("your room rent is =",s,"\n")
    bill=s
    sql="INSERT INTO bill(custname,bill)VALUES('{}','{}')".format(custname,bill)
    mycursor.execute(sql)
    mydb.commit()
def resturentmenuview():
    print("Do yoy want to see mebu available : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        mycursor.execute("select * from resturent")
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
def orderitem():
    print("Do yoy want to see menu available : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        mycursor.execute("select * from resturent")
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
        print("do you want to purchase from above list:enter your choice:")
        d=int(input("enter your choice:"))
        if(d==1):
            print("you have ordered tea")
            a=int(input("enter quantity"))
            s2=10*a
            print("your amount",a,"for tea is :",s2,"\n")
        elif (d==2):
            print("you have ordered coffee")
            a=int(input("enter quantity"))
            s2=10*a
            print("your amount",a,"for coffee is :",s2,"\n")
        elif(d==3):
            print("you have ordered colddrink")
            a=int(input("enter quantity"))
            s2=20*a
            print("your amount",a,"for colddrink is :",s2,"\n")
        elif(d==4):
            print("you have ordered samosa")
            a=int(input("enter quantity"))
            s2=10*a
            print("your amount",a,"for samosa is :",s2,"\n")
        elif(d==5):
            print("you have ordered sandwich")
            a=int(input("enter quantity"))
            s2=50*a
            print('your amount',a,'for sandwich is :',s2,"\n")
        elif(d==6):
            print("you have ordered dhokla")
            a=int(input("enter quantity"))
            s2=30*a
            print("your amount",a,"for dhokla is :",s2,"\n")
        elif(d==7):
            print("you have ordered kachori")
            a=int(input("enter quantity"))
            s2=10*a
            print("your amount",a,"for kachori is :",s2,"\n")
        elif(d==8):
            print("you have ordered milk")
            a=int(input("enter quantity"))
            s2=20*a
            print("your amount",a,"for milk is :",s2,"\n")
        elif(d==9):
            print("you have ordered noodles")
            a=int(input("enter quantity"))
            s2=50*a
            print("your amount",a,"for noodles is :",s2,"\n")
        elif(d==10):
            print("you have ordered pasta")
            a=int(input("enter quantity"))
            s2=50*a
            print("your amount",a,"for pasta is :",s2,"\n")
        else:
            Print("please enter your choice from the menu")
        custname=input('enter custname=')
        bill=s2
        sql="INSERT INTO resbill(custname,bill)VALUES('{}','{}')".format(custname,bill)
    mycursor.execute(sql)
    mydb.commit()
def laundarybill():
    print("Do yoy want to see rate for laundary : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select * from laundary"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
    y=int(input("Enter Your number of clothes->"))
    z=y*10
    print("your laundary bill:",z,"\n")
    custname=input('enter custname')
    lb=z
    sql="INSERT INTO laundarybill(custname,lb)VALUES('{}','{}')".format(custname,lb)
    mycursor.execute(sql)
    mydb.commit()
def viewbill():
    a=input("enter customer name:")
    print("customer name :",a,"\n")
    mycursor.execute("select * from bill")
    x=mycursor.fetchall()
    for i in x:
        if a in i:
            print(i)
    mycursor.execute("select * from laundarybill")
    y=mycursor.fetchall()
    for j in y:
        if a in j:
            print(j)
    mycursor.execute("select * from resbill")
    p=mycursor.fetchall()
    for k in p:
        if a in k:
            print(k)
def Menuset():
    print("enter 1: To enter customer data")
    print("enter 2 : To view roomtype")
    print("enter 3 : for check room bill")
    print("enter 4 : for viewing restaurent menu")
    print("enter 5 : for restaurent bill")
    print("enter 6 :for laundary bill")
    print("enter 7 : for complete bill")
    print("enter 8 : for exit:")
    try:
        userinput=int(input("pleaseselect an above option:"))
    except ValueError:
        exit("\n hi thats not a number")
    userinput=int(input("enter your choice"))
    if(userinput==1):
        registercust()
    elif(userinput==2):
        roomtypeview()
    elif(userinput==3):
        roomrent()
    elif(userinput==4):
        resturentmenuview()
    elif(userinput==5):
        orderitem()
    elif(userinput==6):
        laundarybill()
    elif(userinput==7):
        viewbill()
    elif(userinput==8):
        quit()
    else:
        print("enter correct choice")

    Menuset()
def runagain():
    runagn=input("\n want to run again y/n:")
    while (runagn.lower()=='y'):
        if(platform.system()=="windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        Menuset()
        runagn=input("\n want to run again y/n:")
    runagain()
runagain()



#hotel management.py
#Displaying hotel management.py.
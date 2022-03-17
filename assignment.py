

import requests,json
    
import mysql.connector
from datetime import date

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dronebasenew"
)
mycursor = mydb.cursor()
    
def menu():
    print("Enter your Choice:")
    print("1. Registration 2. Login" )
    ch=int(input("Enter Here:"))
    if ch==1:
        create()
    elif ch==2:
        login()
  
    else:
        print("Wrong Input!!! Please try again....")
        menu()
def update():
    print("Do you know your Id:")
    print("1. Yes 2. No")
    ch=int(input("Enter Choice:"))
    if ch==1:
        ids=int(input("Enter Your Id Here..:"))
        sql="select * from mytable where id=%s"
        val=(ids,)
        mycursor.execute(sql,val)
        myresult=mycursor.fetchall()
        
        for i in myresult:
            fname=i[1]
            lname=i[2]
            email=i[3]
            password=i[4]
          
           
        print("What You Want To Change::")
        print("1. Firstname 2.Lastname 3.Email 4.Password")
        k=int(input("enter ::"))  
        if k == 1: 
            fname=input("Enter Your New Name::")   
        elif k == 2:
            lname=input("Enter Your New Lastname::")
        elif k==3:
            email=input("Enter New Email ::")
        elif k==4:
            password=input("Enter New Password::")
        else:
            print("wrong Input ")
            update()
           
        sql="update mytable set fname=%s,lname=%s ,email=%s,password=%s where id=%s "
        val=(fname,lname,email,password,ids)
        mycursor.execute(sql,val)
        mydb.commit()
          
           
        print("succesfully updated user:")
        mymenu()
            
        
        
       
      
        

        
    elif ch==2:
        read()
        update()
        
    else:
        print("wrong input")
        update()
        


def mymenu():
    print("Welcome:- ")
    print("1. Read 2. Update 3. Delete  4.Check Weather 5. Logout")
    j=int(input("enter choice :"))
    if j==1:
        read()
    elif j==3:
        delete()
    elif j== 2:
        update()
    elif j== 4:
        weather()
    elif j==5:
        menu()
    else:
        print("wrong Input Try again...!!")
        mymenu()
def weather():
    apikey="295308a9716fc6f588b4eb804284aa24"
    baseurl="https://api.openweathermap.org/data/2.5/weather?q="
    CityName=input("Enter Your City::")
    today=date.today()
    url=baseurl+CityName + "&appid=" +apikey
    response=requests.get(url)
    data=response.json()
    print("Humidity::",data["main"]["humidity"])
    print("Pressure::",data["main"]["pressure"])
    print("Average Temperature::",data["main"]["temp"])
    print("Wind Speed::",data["wind"]["speed"])
    print("Wind Degree::",data["wind"]["deg"])
    print("UV Index::",data["visibility"])
    print(today)
    mymenu()
    


    

def read():
    
    mycursor.execute("select * from mytable")
    myresult=mycursor.fetchall()
    print("All Information Given Below:")
    print()
    for i in myresult:
        print("ID=",i[0])
        print("Firstname=",i[1])
        print("Lastname=",i[2])
        print("Email=",i[3])
        print("Password=",i[4])
        print("______________________________________________________")
    mymenu()
def delete():
    print("Do you know your Id:")
    print("1. Yes 2. No")
    print()
    ch=int(input("Enter Choice:"))
    if ch==1:
        ids=int(input("Enter your id:"))
        sql="delete from mytable where id=%s"
        val=(ids,)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Delete Successfully...!!")
        mymenu()
        
    elif ch==2:
        print("Check Your Id::")
        read()
        delete()
        
    


        

def create():
    fname=input("enter your name:")
    lname=input("enter last name:")
    email=input("email:")
    password=input("enter password::")
    sql="insert into mytable (fname,lname,email,password)values(%s,%s,%s,%s)"
    val=(fname,lname,email,password)
    mycursor.execute(sql,val)
    mydb.commit()
    print("succesfully create user:")
    mymenu()
def login():
    email=input("emter your email:")
    password=input("enter password::")
    mycursor.execute("select * from mytable")
    myresult=mycursor.fetchall()
    for i in myresult:
       
        a=str(i[3])
        b=str(i[4])
        if a==email and b==password :
            mymenu()
            break
        else:
            print("Invalid Password or Email Try Again:::")
            print(" press 1. go to menu")
            k=int(input("press::"))
            if k==1:
                menu()
            else:
                print("invalid input")
            login()
    
        
     
   

menu()







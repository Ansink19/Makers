#Connecting to the database
import mysql.connector as sql
con=sql.connect(host='localhost',user='root',passwd='Angads1ngh',database='test')
cursor=con.cursor()
#Calculating Age in Months
def age(year,month):
    from datetime import date
    d=date.today()
    agem=((d.year-year)*12)+(d.month-month)
    return agem
#Calculating Division
def division(age,weight,height):
    grade=(age/9)+((height/3)/2.54)+(weight*0.73)
    if grade>=90:
        return 'O'
    elif grade>=80.01:
        return 'A'
    elif grade>=72.01:
        return 'B'
    elif grade>=64.01:
        return 'C'
    elif grade>=56.01:
        return 'D'
    elif grade>=48.01:
        return 'E'
    elif grade<=48:
        return 'F'
#Creating Table
def ClsTbl():
    print('Enter Details of the Table to be Created: \n')
    cls=input('Please Enter Class: ')
    tbl='create table '+cls+' (Roll_no int , Name char(50), Age int, Height int, Weight int, Division char(2) );'
    cursor.execute(tbl)
    In=input("Would You like to Enter Data in the Table Created[y/n]: \n") #Optional Data Entry
    if In=='y':
        st=int(input("Please Enter Number of Students: "))
        for i in range (st):
            print("Enter Student Details: \n")
            Rn=int(input('Enter Roll No. : '))
            Nm=input('Enter Name: ')
            DOB=input('Enter DOB[DDMMYYYY]: ')
            Age=age(int(DOB[4:]),int(DOB[2:4]))
            Ht=int(input('Enter Height: '))
            Wt=int(input('Enter Weight: '))
            Div=division(Age,Wt,Ht)
            row="insert into "+cls+"(Roll_no,Name,Age,Height,Weight,Division)values( {} ,'{}',{},{},{},'{}')".format(Rn,Nm,Age,Ht,Wt,Div)
            cursor.execute(row)
            con.commit()
#Entering Data in a Table
def Insrt():
    TBL=input("Please Enter The Name of the Table: ")
    st=int(input("Please Enter Number of Students: \n"))
    for i in range (st):
        print("Enter Student Details: \n")
        Rn=int(input('Enter Roll No. : '))
        Nm=input('Enter Name: ')
        DOB=input('Enter DOB[DDMMYYYY]: ')
        Age=age(int(DOB[4:]),int(DOB[2:4]))
        Ht=int(input('Enter Height: '))
        Wt=int(input('Enter Weight: '))
        Div=division(Age,Wt,Ht)
        row="insert into "+TBL+"(Roll_no,Name,Age,Height,Weight,Division)values( {} ,'{}',{},{},{},'{}')".format(Rn,Nm,Age,Ht,Wt,Div)
        cursor.execute(row)
        con.commit()
#Entering Events
def events():
    CLS=input("Please Enter Class ")
    tbl1='create table '+CLS+'events (Roll_no int , Name char(50),Age int ,Height int, Weight int, Division char(2) );'
    cursor.execute(tbl1)
    data="insert into "+CLS+"events select * from " +CLS+" ;"
    cursor.execute(data)
    con.commit()
    data1="alter table "+CLS+"events add(Event1 char(50) ,Event2 char(50), Event3 char(50), CrsCntry char(50));"
    cursor.execute(data1)
    students=int(input("Enter Number of students: \n"))
    for j in range (students):
        print("Please Enter Details: \n")
        rollno=int(input("Enter Roll_No: "))
        Asd=eval(input("Enter Events([...,....,....]): "))
        cntry=input("Has the Student Taken Cross Country(y/n): ")
        entry1="update "+CLS+"events set Event1='{}' where Roll_no={}".format(Asd[0],rollno)
        cursor.execute(entry1)
        con.commit()
        entry2="update "+CLS+"events set Event2='{}' where Roll_no={}".format(Asd[1],rollno)
        cursor.execute(entry2)
        con.commit()
        entry3="update "+CLS+"events set Event3='{}' where Roll_no={}".format(Asd[2],rollno)
        cursor.execute(entry3)
        con.commit()
        entry4="update "+CLS+"events set CrsCntry='{}' where Roll_no={}".format(cntry,rollno)
        cursor.execute(entry4)
        con.commit()
    

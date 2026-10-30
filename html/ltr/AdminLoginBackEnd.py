#!C:\Python312\python.exe
import cgi
import cgitb
import os
cgitb.enable()
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
# print(form)
Email=form.getvalue("Email")
# print(Email)
Password=form.getvalue("Password")
# print(Password)
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="royalbakers")
mycursor = mydb.cursor()
query=f""" select * from adminlogin where Email='{Email}' AND Password='{Password}' """
# print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()
# print(myresult)
if mycursor.rowcount==1:
    print(f'''
    <script>
    localStorage.clear();
    localStorage.setItem("id",'{myresult[0]}');
    localStorage.setItem("Email",'{myresult[1]}');
    localStorage.setItem("username",'{myresult[3]}');
    alert("Login Successfully!!!");
    location.href="UnitList.py";
    </script>''')
else:
    print(f'''
    <script>alert("Login Unsuccessfully!");
    location.href="AdminLogin.py";
    </script>''')
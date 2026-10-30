#!C:\Python312\python.exe
import cgi
import cgitb
import os
cgitb.enable()
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
# print(form)
id=form.getvalue("id")
# print(id)
Email=form.getvalue("Email")
# print(Email)
Password=form.getvalue("Password")
# print(Password)
username=form.getvalue("username")
# print(username)
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="royalbakers")
mycursor = mydb.cursor()
query=f""" update adminlogin set Email='{Email}',Password='{Password}',username='{username}' where id='{id}' """
# print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert("Admin Information Changed Successfully!");
    location.href="AdminLogin.py";
    </script>''')

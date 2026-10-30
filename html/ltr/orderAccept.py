#!C:\Python312\python.exe
import cgi
import cgitb
import os
cgitb.enable()
print("Content-Type:text/html\n")
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="royalbakers")
mycursor=mydb.cursor()
form=cgi.FieldStorage()
#print(form)
id=form.getvalue("id")
#print(id) 
query=f""" Update ordermaster set status="Accepted" where id='{id}' """
#print(query)

mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert("Order Accepted Successfully!");
    location.href="allOrders.py";
    </script>''')

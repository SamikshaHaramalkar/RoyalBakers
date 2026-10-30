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
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="royalbakers")
mycursor = mydb.cursor()
query=f"""delete from category where id={id}"""
# print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert("Category Deleted Successfully!");
    location.href="CategoryList.py";
    </script>''')


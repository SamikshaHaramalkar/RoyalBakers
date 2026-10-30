#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="royalbakers")
mycursor = mydb.cursor()

form=cgi.FieldStorage()
#print(form)

id=form.getvalue("id")
FirstName=form.getvalue("FirstName")
MiddleName=form.getvalue("MiddleName")
LastName=form.getvalue("LastName")
PhoneNo=form.getvalue("PhoneNo")
Email=form.getvalue("Email")
Password=form.getvalue("Password")

query=f""" Update registration set FirstName='{FirstName}',
MiddleName='{MiddleName}',LastName='{LastName}',
PhoneNo='{PhoneNo}',Email='{Email}',Password='{Password}' 
WHERE id='{id}' """
#print(query)

mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert("User Information Update Successfully!");
    location.href="Logout.py";
    </script>''')
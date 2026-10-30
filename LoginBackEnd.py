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
Email=form.getvalue("Email")
Password=form.getvalue("Password")
query=f""" SELECT * from registration where Email='{Email}' AND Password='{Password}' """
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()
if mycursor.rowcount==1:
    print(f'''
    <script>
    localStorage.clear();
    localStorage.setItem("id",'{myresult[0]}');     
    localStorage.setItem("FirstName",'{myresult[1]}');
    localStorage.setItem("Photo",'{myresult[7]}');
    alert("Login Successfully!!!");
    location.href="home.py";
    </script>''')
else:
    print(f'''
    <script>alert("Login Unsuccessfully!");
    location.href="Login.py";
    </script>''')
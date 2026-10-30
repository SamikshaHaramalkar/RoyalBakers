#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
# print(form)
FlavourName=form.getvalue("FlavourName")
#print(FlavourName)
Status=form.getvalue("Status")
#print(Status)
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="royalbakers")
mycursor = mydb.cursor()
query=f"""insert into flavour(FlavourName,Status) VALUES('{FlavourName}','{Status}') """
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert("Flavour Added Successfully!");
    location.href="FlavourList.py";
    </script>''')
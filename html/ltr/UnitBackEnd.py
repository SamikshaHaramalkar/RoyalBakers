#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
# print(form)
UnitName=form.getvalue("UnitName")
#print(UnitName)
Discription=form.getvalue("Discription")
#print(Discription)
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="royalbakers")
mycursor = mydb.cursor()
query=f"""insert into unit(UnitName,Discription) VALUES('{UnitName}','{Discription}') """
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert("Unit Added Successfully!");
    location.href="UnitList.py";
    </script>''')
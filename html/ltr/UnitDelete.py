#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
#print(form)
id=form.getvalue("id")
#print(id)
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="royalbakers")
mycursor = mydb.cursor()
query=f"""delete from unit where id={id}"""
# print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert("Unit Deleted Successfully!");
    location.href="UnitList.py";
    </script>''')

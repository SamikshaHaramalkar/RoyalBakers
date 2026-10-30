#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
# print(form)
id=form.getvalue("id")
#print(id)
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
query=f"""update unit set UnitName='{UnitName}',Discription='{Discription}' where id='{id}'"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert("Unit Name Updated Successfully !!");
    location.href="UnitList.py";
    </script>''')
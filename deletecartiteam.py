#!C:/Python312/python.exe
import cgi 
import cgitb 
cgitb.enable() 
print("Content-Type:text/html\n")
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="royalbakers")
#print(mydb)
mycursor=mydb.cursor()


form=cgi.FieldStorage()
id=form.getvalue("id")
#print(id)
userid=form.getvalue("userid")
#print(userid)




query=f""" DELETE FROM cart WHERE id='{id}'"""
#print(query)


mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert("Item deleted Successfully!");
    location.href="cartdetail.py?userid={userid}";
    </script>''')
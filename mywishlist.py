#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
form=cgi.FieldStorage()
#print(form)
userid=form.getvalue("userid")
#print(id)
productid=form.getvalue("productid")
#print(productid)
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="royalbakers")
mycursor = mydb.cursor()
query=f""" INSERT INTO wishlist (userid,productid) VALUES ('{userid}','{productid}')"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert("Product add to wishlist successfully!");
    location.href="Product.py";
    </script>''')
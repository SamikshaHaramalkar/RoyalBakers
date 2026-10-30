#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
#print("Content-Type: text/html\n")


form=cgi.FieldStorage()
#print(form)


quantity=form.getvalue("quantity")
userid=form.getvalue("userid")
proid=form.getvalue("proid")
ProductName=form.getvalue("ProductName")
Price=form.getvalue("Price")
#print(Price)
Photo=form.getvalue("Photo")


print("Content-Type: text/html\n")
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="royalbakers")
mycursor = mydb.cursor()

query=f""" INSERT INTO cart (quantity,userid,proid,ProductName,Price,Photo)
VALUES('{quantity}','{userid}','{proid}','{ProductName}','{Price}','{Photo}')"""
#print(query)


mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert("Product Add to Cart Successfully!");
    location.href="cartdetail.py?userid={userid}";
    </script>''')
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
form = cgi.FieldStorage()
userid=form.getvalue("userid") 
status="Pending"
query = f"""SELECT * FROM cart WHERE userid='{userid}'"""
mycursor.execute(query)
myresult = mycursor.fetchall()
#print(myresult)
grand_total = 0
for x in myresult:
    Price = int(x[5])
    quantity = int(x[1])
    grand_total += Price *quantity
query1 = f"""INSERT INTO ordermaster (userid, total_amount, status)
           VALUES ('{userid}','{grand_total}','{status}')"""
mycursor.execute(query1)
order_id = mycursor.lastrowid
#print(order_id)
for x in myresult:
    proid = x[3]
    ProductName=x[4]
    Photo=x[6]
    Price = int(x[5])
    quantity = int(x[1])
    total = Price * quantity
    query2 = f"""INSERT INTO order_details 
               (order_id, proid,ProductName,Photo,Price, quantity, total)
               VALUES ('{order_id}','{proid}','{ProductName}','{Photo}','{Price}','{quantity}','{total}')"""
    mycursor.execute(query2)
query3 = f"""DELETE FROM cart WHERE userid='{userid}'"""
mycursor.execute(query3)
mydb.commit()
print(f'''
    <script>alert("Order Placed Successfully!");
    location.href="Product.py";
    </script>''')

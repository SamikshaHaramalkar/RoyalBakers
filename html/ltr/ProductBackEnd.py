#!C:/Python312/python.exe
import cgi 
import cgitb 
import os
cgitb.enable() 
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
# print(form)
ProductName=form.getvalue("ProductName")
# print(ProductName)
CategoryName=form.getvalue("CategoryName")
# print(CategoryName)
FlavourName=form.getvalue("FlavourName")
# print(FlavourName)
UnitName=form.getvalue("UnitName")
# print(UnitName)
Price=form.getvalue("Price")
# print(Price)
Discription=form.getvalue("Discription")
# print(Discription)
fi=form["Photo"]
#print(fi.filename)
fn=os.path.splitext(fi.filename)
# print(fn[1])
UploadFileName='abc'+fn[1]
#print(UploadFileName)
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="royalbakers")
mycursor = mydb.cursor()
query=f""" insert into product(ProductName,CategoryName,FlavourName,UnitName,Price,Discription,Photo) 
VALUES('{ProductName}','{CategoryName}','{FlavourName}','{UnitName}','{Price}','{Discription}','{UploadFileName}')"""
# print(query)
mycursor.execute(query)
mydb.commit()
pro_id=mycursor.lastrowid
# print(pro_id)
upload_dir=f"""Product/{pro_id}"""
# print(upload_dir)
os.makedirs(upload_dir,exist_ok=True)
file_path=os.path.join(upload_dir,UploadFileName)
# print(file_path)
open(file_path,'wb').write(fi.file.read())
print(f'''
    <script>alert("Product Added Successfully!");
    location.href="ProductList.py";
    </script>''')























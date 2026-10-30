#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
form=cgi.FieldStorage()
#print(form)
FirstName=form.getvalue("FirstName")
MiddleName=form.getvalue("MiddleName")
LastName=form.getvalue("LastName")
PhoneNo=form.getvalue("PhoneNo")
Email=form.getvalue("Email")
Password=form.getvalue("Password")
fi=form["Photo"]
import os
fn=os.path.splitext(fi.filename)
#print(fn[0])
UploadFileName='abc'+fn[1]
#print(UploadFileName)
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="royalbakers")
mycursor = mydb.cursor()
query=f""" INSERT INTO registration (FirstName,MiddleName,LastName,PhoneNo,Email,Password,Photo)VALUES('{FirstName}','{MiddleName}','{LastName}','{PhoneNo}','{Email}','{Password}','{UploadFileName}')"""
#print(query)
mycursor.execute(query)
reg_id=mycursor.lastrowid
# print(reg_id)
upload_dir=f"""Registration/{reg_id}"""
#print(upload_dir)
os.makedirs(upload_dir,exist_ok=True)
file_path=os.path.join(upload_dir,UploadFileName)
#print(file_path)
open(file_path,'wb').write(fi.file.read())
mydb.commit()
print(f'''
    <script>alert("Your Account Created Successfully!");
    location.href="Login.py";
    </script>''')


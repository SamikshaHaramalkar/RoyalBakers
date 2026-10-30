#!C:\Python312\python.exe
import cgi
import cgitb
import os
cgitb.enable()
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
# print(form)
CategoryName=form.getvalue("CategoryName")
# print(CategoryName)
Discription=form.getvalue("Discription")
# print(Discription)
fi=form["Photo"]
# print(fi)
fn=os.path.splitext(fi.filename)
# print(fn[1])
UploadFileName='abc'+fn[1]
# print(UploadFileName)
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="royalbakers")
mycursor = mydb.cursor()
query=f""" insert into category(CategoryName,Discription,Photo) VALUES('{CategoryName}','{Discription}','{UploadFileName}')"""
# print(query)
mycursor.execute(query)
mydb.commit()
cat_id=mycursor.lastrowid
# print(cat_id)
upload_dir=f"""Category/{cat_id}"""
# print(upload_dir)
os.makedirs(upload_dir,exist_ok=True)
file_path=os.path.join(upload_dir,UploadFileName)
# print(file_path)
open(file_path,'wb').write(fi.file.read())
print(f'''
    <script>alert("Category Added Successfully!");
    location.href="CategoryList.py";
    </script>''')

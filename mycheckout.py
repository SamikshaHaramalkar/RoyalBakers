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
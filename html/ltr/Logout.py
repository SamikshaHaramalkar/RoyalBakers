#!C:\Python312\python.exe
import cgi
import cgitb
import os
cgitb.enable()
print("Content-Type:text/html\n")
print(f'''
    <script>
    localStorage.clear();
    alert("Log-Out Successfully!");
    location.href="AdminLogin.py";
    </script>''')

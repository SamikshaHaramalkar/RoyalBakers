#!C:/Python312/python.exe
import cgi 
import cgitb 
cgitb.enable() 
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="royalbakers")
mycursor = mydb.cursor()
query=f""" select * from category"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
query1=f""" select * from flavour"""
#print(query1)
mycursor.execute(query1)
myresult1=mycursor.fetchall()
#print(myresult1)
query2=f""" select * from unit"""
#print(query2)
mycursor.execute(query2)
myresult2=mycursor.fetchall()
#print(myresult2)
options_html = '<option value="">Select Category Name</option>\n'
for x in myresult:
    CategoryName = x[1]
    options_html += f'<option value="{CategoryName}">{CategoryName}</option>\n'
options_flavour = '<option value="">Select Flavour Name</option>\n'
for x in myresult1:
    FlavourName = x[1]
    options_flavour += f'<option value="{FlavourName}">{FlavourName}</option>\n'
options_unit = '<option value="">Select Unit Name</option>\n'
for x in myresult2:
    UnitName = x[1]
    options_unit += f'<option value="{UnitName}">{UnitName}</option>\n'
import Header
print(f"""


        <!-- ============================================================== -->
        <!-- End Left Sidebar - style you can find in sidebar.scss  -->
        <!-- ============================================================== -->
        <!-- ============================================================== -->
        <!-- Page wrapper  -->
        <!-- ============================================================== -->
        <div class="page-wrapper">
            <!-- ============================================================== -->
            <!-- Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <div class="page-breadcrumb">
                <div class="row">
                    <div class="col-5 align-self-center">
                        <h4 class="page-title">Product Master</h4>
                        <div class="d-flex align-items-center">
                            <nav aria-label="breadcrumb">   
                            </nav>
                        </div>
                    </div>
                </div>
            </div>
            <!-- ============================================================== -->
            <!-- End Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <!-- ============================================================== -->
            <!-- Container fluid  -->
            <!-- ============================================================== -->
            <div class="container-fluid">
                <!-- ============================================================== -->
                <!-- Start Page Content -->
                <!-- ============================================================== -->
                <!-- row -->
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">

                                <h4 class="card-title">Product Form</h4>
                               
                                <form class="m-t-30" action="ProductBackEnd.py" method="POST" enctype="multipart/form-data" >  
                                    <div class="form-group">
                                        <label for="exampleInputEmail1">Product Name :</label>
                                        <input type="text" class="form-control" id="ProductName" name="ProductName" aria-describedby="emailHelp" placeholder="Enter Product Name">
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1">Category Name :</label>
                                        <select name="CategoryName" id="CategoryName" class="form-control">
                                        {options_html}
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1">Flavour Name :</label>
                                        <select name="FlavourName" id="FlavourName" class="form-control">
                                        {options_flavour}
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1">Unit Name :</label>
                                       <select name="UnitName" id="UnitName" class="form-control">
                                        {options_unit}
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1">Price :</label>
                                        <input type="text" class="form-control" id="Price" name="Price" placeholder="Enter Price">
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1">Discription :</label>
                                        <input type="text" class="form-control" id="Discription" name="Discription" placeholder="Enter Discription">
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1">Product Image :</label>
                                        <input type="file" class="form-control" id="Photo" name="Photo" placeholder="choose correct product">
                                    </div>
                                    

                                   
                                    <button type="submit" class="btn btn-primary" style="background-color:#fb8c00;border:2px solid black">Submit</button>
                                </form>
                                
                            </div>
                        </div>
                    </div>
                </div>
                <!-- row -->
                <!-- .row -->
               
                <!-- /.row -->
                <!-- Row -->
                
                <!-- Row -->
                <!-- .row -->

                
                <!-- /.row -->
                <!-- .row -->
               
                <!-- /.row -->
                <!-- .row -->
               
                <!-- .row -->
                
                <!-- /.row -->
                
                <!-- row -->
                <!-- Row -->
               
                <!-- Row -->
                <!-- ============================================================== -->
                <!-- End PAge Content -->
                <!-- ============================================================== -->
                <!-- ============================================================== -->
                <!-- Right sidebar -->
                <!-- ============================================================== -->
                <!-- .right-sidebar -->
                <!-- ============================================================== -->
                <!-- End Right sidebar -->
                <!-- ============================================================== -->
            </div>
            <!-- ============================================================== -->
            <!-- End Container fluid  -->
            <!-- ============================================================== -->
            <!-- ============================================================== -->
            <!-- footer -->
            <!-- ============================================================== -->
            
""")
import Footer
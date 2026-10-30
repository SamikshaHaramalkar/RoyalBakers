#!C:/Python312/python.exe
import cgi 
import cgitb 
cgitb.enable() 
import Header
print("""


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
                        <h4 class="page-title">Category Master</h4>
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

                                <h4 class="card-title">Category Form</h4>
                               
                                <form class="m-t-30" action="CategoryBackEnd.py" method="POST" enctype="multipart/form-data" > 
                                   
                                    <div class="form-group">
                                        <label for="exampleInputEmail1">Category Name :</label>
                                        <input type="text" class="form-control" id="CategoryName" name="CategoryName" aria-describedby="emailHelp" placeholder="Enter Category Name">
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1">Discription :</label>
                                        <input type="text" class="form-control" id="Discription" name="Discription" placeholder="Enter Discription">
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1">Category Image</label>
                                        <input type="file" class="form-control" id="Photo" name="Photo">
                                    </div>
                            
                                   
                                    <button type="submit" class="btn btn-primary" style="background-color:#fb8c00;border:2px solid black" >Submit</button>
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
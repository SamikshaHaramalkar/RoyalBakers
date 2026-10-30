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
                        <h4 class="page-title">Flavour Master</h4>
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

                                <h4 class="card-title">Flavour Form</h4>
                               
                                <form class="m-t-30" action="FlavourBackEnd.py" method="POST"> 
                                    <div class="form-group">
                                        <label for="exampleInputEmail1">Flavour Name :</label>
                                        <input type="text" class="form-control" id="FlavourName" name="FlavourName" aria-describedby="emailHelp" placeholder="Enter Flavour Name">
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1">Status :</label>
                                        <input type="text" class="form-control" id="Status" name="Status" placeholder="Enter Status">
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
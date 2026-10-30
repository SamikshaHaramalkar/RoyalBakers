#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
 
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="royalbakers")
mycursor = mydb.cursor()

mycursor1 = mydb.cursor(dictionary =True)


query1=""" SELECT COUNT(*) FROM product """
#print(query1)
mycursor.execute(query1)
myresult1= mycursor.fetchone()[0]
#print(myresult1)

query2=""" SELECT COUNT(*) FROM category """
#print(query2)
mycursor.execute(query2)
myresult2= mycursor.fetchone()[0]
#print(myresult2)


query3=""" SELECT COUNT(*) FROM registration """
#print(query3)
mycursor.execute(query3)
myresult3= mycursor.fetchone()[0]
#print(myresult3)

query4=""" SELECT COUNT(*) FROM ordermaster """
#print(query4)
mycursor.execute(query4)
myresult4= mycursor.fetchone()[0]
#print(myresult4)


query5=""" SELECT COUNT(*) FROM ordermaster WHERE status="Pending" """
#print(query5)
mycursor.execute(query5)
myresult5= mycursor.fetchone()[0]
#print(myresult5)

query6=""" SELECT COUNT(*) FROM ordermaster WHERE status="Accepted" """
#print(query6)
mycursor.execute(query6)
myresult6= mycursor.fetchone()[0]
#print(myresult6)

query7=""" select count(id) as pcount,`CategoryName` from product GROUP BY `CategoryName` """
#print(query7)
mycursor1.execute(query7)
myresult7= mycursor1.fetchall()
#print(myresult7)
procount=''
for x in myresult7:
    procount+=f""" ['{x['CategoryName']}',    {x['pcount']}], """

query8=""" SELECT
    SUM(total_amount) AS daytotal,
    DATE(order_date) AS order_date
FROM ordermaster
WHERE DATE(order_date) BETWEEN CURRENT_DATE() - INTERVAL 7 DAY AND CURRENT_DATE()
GROUP BY DATE(order_date)
ORDER BY DATE(order_date) """
#print(query8)
mycursor1.execute(query8)
myresult8= mycursor1.fetchall()
#print(myresult8)
weeklysale=''
for x in myresult8:
    weeklysale+=f""" ['{x['order_date']}',    {x['daytotal']}], """





import Header
print("""
 <!----Sales chart start----->
 <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Weak Days', 'Sales'],
         """ + weeklysale +"""
         
        ]);

        var options = {
          title: 'Royal Bakers  Performance',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

        chart.draw(data, options);
      }
    </script>
    <!----Sales chart end----->



<!----Category wise product start-------------->
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Category Name', 'Product Count'],
           """ + procount + """
        ]);

        var options = {
          title: 'My Categries Wise Product Count'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }
    </script>
<!---------Category wise product end--------------->
""")
print(f"""
    <div class="page-wrapper">
            <!-- ============================================================== -->
            <!-- Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <div class="page-breadcrumb" style="border-bottom:2px solid black;">
                <div class="row">
                    <div class="col-5 align-self-center" >
                        <h4 class="page-title">Dashboard</h4>
                        
                        <div class="d-flex align-items-center">
                            <nav aria-label="breadcrumb">
                              
                            </nav>
                        </div>
                        
                    </div>
                     
                </div>
            </div>

    <div class="container-fluid">
             <div class="card-body">
                                <!-- title -->
                                <div class="d-md-flex align-items-center">
                                    <div>
                                        <h4 class="card-title" style="color: #eb2328;">Quick Summary of Your Bakery Store</h4>
                                           </div>
                                     
                                </div>
                                <!-- title -->
            </div>
               
                <div class="row">
                    <!-- crypto -->
                    
                    <div class="col-sm-12 col-lg-4">
                        <div class="card bg-orange">
                            <div class="card-body">
                                <div class="d-flex align-items-center">
                                    <div class="m-r-10">
                                        <h1 class="m-b-0"> <img src="icons/1.png" style="width:80px;"></h1></div>
                                    <div>
                                        <h6 class="m-b-5 op-7" style="font-size:20px;color:black"> Total Products</h6>
                                        <h6 class="text-white  m-b-0" style="font-size:30px;text-align: center;">{myresult1}</h6>
                                    </div>
                                    
                                </div>
                                
                            </div>
                        </div>
                    </div>


                     <div class="col-sm-12 col-lg-4">
                        <div class="card " style="background-color:#bf0ab9 !important">
                            <div class="card-body">
                                <div class="d-flex align-items-center">
                                    <div class="m-r-10">
                                        <h1 class="m-b-0"> <img src="icons/2.png" style="width:80px;"></h1></div>
                                    <div>
                                        <h6 class="m-b-5 op-7" style="font-size:20px;color:black">Total Categories</h6>
                                        <h6 class="text-white  m-b-0" style="font-size:30px;text-align: center;">{myresult2}</h6>
                                    </div>
                                    
                                </div>
                                
                            </div>
                        </div>
                    </div>


                     <div class="col-sm-12 col-lg-4">
                        <div class="card " style="background-color:var(--purple) !important">
                            <div class="card-body">
                                <div class="d-flex align-items-center">
                                    <div class="m-r-10">
                                        <h1 class="m-b-0"> <img src="icons/3.png" style="width:80px;"></h1></div>
                                    <div>
                                        <h6 class="m-b-5 op-7" style="font-size:20px;color:black">Total Customers</h6>
                                        <h6 class="text-white  m-b-0" style="font-size:30px;text-align: center;">{myresult3}</h6>
                                    </div>
                                    
                                </div>
                                
                            </div>
                        </div>
                    </div>

                </div>






                <div class="card-body">
                                <!-- title -->
                                <div class="d-md-flex align-items-center">
                                    <div>
                                        <h4 class="card-title" style="color: #eb2328;">Order Summary</h4>
                                           </div>
                                     
                                </div>
                                <!-- title -->
                </div>



                        <div class="row">
                    <!-- crypto -->
                    
                    <div class="col-sm-12 col-lg-4">
                        <div class="card" style="background-color:var(--teal) !important;">
                            <div class="card-body">
                                <div class="d-flex align-items-center">
                                    <div class="m-r-10">
                                        <h1 class="m-b-0"> <img src="icons/4.png" style="width:80px;"></h1></div>
                                    <div>
                                        <h6 class="m-b-5 op-7" style="font-size:20px;color:black"> Total Orders</h6>
                                        <h6 class="text-white  m-b-0" style="font-size:30px;text-align: center;">{myresult4}</h6>
                                    </div>
                                    
                                </div>
                                
                            </div>
                        </div>
                    </div>


                     <div class="col-sm-12 col-lg-4">
                        <div class="card " style="background-color:#ef240f !important">
                            <div class="card-body">
                                <div class="d-flex align-items-center">
                                    <div class="m-r-10">
                                        <h1 class="m-b-0"> <img src="icons/5.png" style="width:80px;"></h1></div>
                                    <div>
                                        <h6 class="m-b-5 op-7" style="font-size:20px;color:black">Pending Orders</h6>
                                        <h6 class="text-white  m-b-0" style="font-size:30px;text-align: center;">{myresult5}</h6>
                                    </div>
                                    
                                </div>
                                
                            </div>
                        </div>
                    </div>


                     <div class="col-sm-12 col-lg-4">
                        <div class="card " style="background-color:#21ab08 !important">
                            <div class="card-body">
                                <div class="d-flex align-items-center">
                                    <div class="m-r-10">
                                        <h1 class="m-b-0"> <img src="icons/6.png" style="width:80px;"></h1></div>
                                    <div>
                                        <h6 class="m-b-5 op-7" style="font-size:20px;color:black">Accepted Orders</h6>
                                        <h6 class="text-white  m-b-0" style="font-size:30px;text-align: center;">{myresult6}</h6>
                                    </div>
                                    
                                </div>
                                
                            </div>
                        </div>
                    </div>

                </div>



<div class="row">
                    <!-- column -->
                    <div class="col-sm-12 col-lg-6">
                        <div class="card card-hover">
                            <div class="card-body">
                                <h4 class="card-title">Sales Summary</h4>
                                 
                                
                                <div id="curve_chart" style="width: 500px; height: 500px"></div>
                            </div>
                        </div>
                    </div>
                    <!-- column -->
                    <div class="col-sm-12 col-lg-6">
                        <div class="card card-hover">
                            <div class="card-body">
                                <h4 class="card-title">Category-wise Products</h4>

                                  <div id="piechart" style="width: 500px; height: 500px;"></div>
                                
                            </div>
                        </div>
                    </div>
                   
                </div>




























    </div>
                    
""")
import Footer




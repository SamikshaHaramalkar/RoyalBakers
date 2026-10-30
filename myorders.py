#!C:/Python312/python.exe
import cgi 
import cgitb 
cgitb.enable() 
#print("Content-Type:text/html\n")
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="royalbakers")
#print(mydb)
mycursor=mydb.cursor()


form=cgi.FieldStorage()
userid=form.getvalue("userid")
#print(userid)


query = f"""
SELECT
    om.id,
    om.order_date,
    om.status,
    od.ProductName,
    od.proid,
    od.Photo,
    od.price,
    od.quantity,
    od.total
FROM ordermaster om
INNER JOIN order_details od
ON om.id = od.order_id
WHERE om.userid = '{userid}'
"""
#print(query)


mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)


tr_html=''
for x in myresult:
    color = "black"
    if x[2] == "Pending":
        color = "red"
    elif x[2] == "Completed":
        color = "green"
    tr_html+=f"""
                    <!---for loop row star---->
                                    <div class="wishlist-area">
                                        <div class="wishlist-details">
                                            
                                            <div class="wishlist-all-pro">
                                                <div class="wishlist-pro" style="width:100%">
                                                    <div class="wishlist-pro-image" style="width:100%">
                                                        <a href="">
                                                            <img src="html/ltr/Product/{x[4]}/{x[5]}" class="img-fluid" alt="p-1" style="width:150px">
                                                        </a>
                                                    </div>
                                                    <div class="pro-details">
                                                        <h4>{x[3]}</h4>
                                                    </div>

                                                   

                                                     
                                                     <div class="pro-details">
                                                        <h4> {x[6]} </h4> 
                                                    </div>

                                                     <div class="pro-details">
                                                        <h4> {x[7]} </h4> 
                                                    </div>

                                                     <div class="pro-details">
                                                        <h4 style='color:{color}; font-weight:bold;'> {x[2]} </h4> 
                                                    </div>
                                                     
                                                      </div>
                                                 
                                                 
                                            </div>
                                        </div>
                                    </div>
                                   <!--- for loop row end----->
    """
import header

print(f"""
 <section class="order-histry-area section-ptb">
                <div class="container">
                    <div class="row">
                        
                            <div>
                               
                                <!-- profile-wishlist start -->
                                <div class="profile-wishlist">
                                    <div class="section-capture">
                                <div class="section-title">
                                    <span class="sub-title">All Orders</span>
                                    <h2><span>My Orders</span></h2>
                                </div>
                            </div>

                            {tr_html}
                                </div>
                                <!-- profile-wishlist end -->
                            </div>
                         
                    </div>
                </div>
            </section>
""")

import footer




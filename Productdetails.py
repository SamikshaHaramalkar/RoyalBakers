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

form=cgi.FieldStorage()
proid=form.getvalue("proid")

query=f""" SELECT * FROM Product WHERE id='{proid}' """
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()
#print(myresult)


import header
print(f"""
 <section class="product-details-page pro-style1">
                <div class="container">
                    <div class="row">
                        <div class="col">
                            <div class="pro_details_pos pro_details_left_pos">
                                <!-- Product slider start -->
                                <div class="product_detail_slider product_details_tb product_details product_details_sticky">
                                    
                                    <img src="html/ltr/Product/{myresult[0]}/{myresult[7]}" style="width:100%;height:50%;">
                                </div>
                                <!-- peoduct detail start -->
                                <div class="product_details_wrap product_details_tb product_details">
                                    <div class="product_details_info">
                                        <div class="pro-nprist">
                                            
                                            <div class="product-info">
                                                
                                                <div class="product-title">
                                                    <h2>{myresult[1]}</h2>
                                                </div>
                                                 
                                            </div>
                                            <div class="product-info">
                                                <div class="pro-prlb pro-sale">
                                                    <div class="price-box">
                                                        <span class="new-price">{myresult[5]} /-RS.</span>
                                                        
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="product-info">
                                                <div class="product-inventory">
                                                    <p> {myresult[6]}</p>
                                                    <div class="product-variant">
                                                        <h6>Availability:</h6>
                                                       
                                                        <span class="stock-qty in-stock text-success">
                                                            <span>In stock<i class="bi bi-check2"></i></span>
                                                        </span>
                                                        
                                                    </div>
                                                     <div class="product-variant">



                                                    <form action="cart.py" method="POST">

                                                    <lable>Enter Required Quantity</lable><br>
                                                    <input type="text" id="quantity" name="quantity" required>
                                                    <input type="hidden" id="userid" name="userid" required>
                                                    <input type="hidden" id="proid" name="proid" required value="{myresult[0]}">
                                                    <input type="hidden" id="ProductName" name="ProductName" required value="{myresult[1]}">
                                                   <input type="hidden" id="Price" name="Price" required value="{myresult[5]}">
                                                     <input type="hidden" id="Photo" name="Photo" required value="{myresult[7]}">
                                                   
                                                    
                                                    




                                                    </div>
                                                </div>
                                            </div>
                                           
                                           
                                            <div class="product-info">
                                                <div class="product-actions">
                                                    <!-- pro-deatail button start -->
                                                    <div class="pro-detail-button">
                                                        <button type="submit" class="btn btn-style2">
                                                        <span class="cart-title">Add to cart</span>
                                                        </button>
                                                        
                                                    </div>
                                                    </form>
                                                     
                                                </div>
                                            </div>
                                           
                                           
                                            
                                             
                                            
                                        </div>
                                    </div>
                                </div>
                                <!-- peoduct detail end -->
                            </div>
                        </div>
                    </div>
                </div>
            </section>


            
""")
import footer
print("""
<script>
document.addEventListener("DOMContentLoaded", function () {
    let userid = localStorage.getItem("id");

    if(userid){
        document.getElementById("userid").value = userid;
    }
});
</script>
""")



 

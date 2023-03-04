import os

from cs50 import SQL
from flask import Flask, json, redirect, render_template, request, session, flash
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required


# Configure application
app = Flask (__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS%) Library to use SQLite database
db = SQL("sqlite:///customer.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cach, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Render register.html
    if request.method == "GET":
        return render_template("register.html")

    # Ensure first name is not blank
    if request.form.get("fname") == "":
        return apology("must provide first name", 400)

    # Ensure last name is not blank
    if request.form.get("lname") == "":
        return apology("must provide last name", 400)

    # Ensure username is not blank
    if request.form.get("username") == "":
        return apology("must provide username", 400)

    # Ensure password is not blank
    if request.form.get("password") == "":
        return apology("must provide password", 400)

    # Ensure confirm password is not blank
    if request.form.get("confirm") == "":
        return apology("must confirm password", 400)

    # Ensure password and confirmation password match
    if not request.form.get("password") == request.form.get("confirm"):
        return apology("passwords must match", 400)

    # Ensure email is not blank
    if request.form.get("useremail") == "":
        return apology("must provide email", 400)

    # Ensure username does not already exist
    if db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username")):
        return apology("username already exists", 400)

    # Put user input into variables
    firstname = request.form.get("fname")
    lastname = request.form.get("lname")
    email = request.form.get("useremail")
    username = request.form.get("username")
    userpassword = request.form.get("password")

    # Hash password
    hashkey = generate_password_hash(userpassword)

    # Insert username and passord into finance.db
    db.execute("INSERT INTO users (firstname, lastname, username, email, hash) VALUES(?,?,?,?,?)", firstname, lastname, username, email, hashkey)

    # Go to login.html
    if request.method == "POST":
        flash("You are registered!")
        return render_template("login.html")


@app.route("/")
@login_required
def index():
    """Show home page"""

    id = session["user_id"]

    # User reached route via login
    if request.method == "GET":     
        # return render_template("index.html") to include first name of user
        firstname = db.execute("SELECT firstname from users WHERE id = ?", id)
        userfirstname = firstname[0]['firstname']
        return render_template("index.html", userfirstname=userfirstname)


@app.route("/view", methods=['GET'])
@login_required
def view():
    """Show portfolio of images"""

    id = session["user_id"]
        
    # return render_template("view.html") to include budget of user
    if db.execute("SELECT firstname from users WHERE id = ?", id):
        firstname = db.execute("SELECT firstname from users WHERE id = ?", id)
        userfirstname = firstname[0]['firstname']
        return render_template("view.html", userfirstname=userfirstname)


@app.route("/test", methods=['POST'])
@login_required
def test():
    """Retrieve cart variable from javascript"""

    id = session["user_id"]

    if request.method == "POST":
        
        # Fetch product ID from json
        output = request.get_json()
        result = json.loads(output)
        
        # Look up product ID on database and return information for temporary table cart
        cart = db.execute("SELECT product_id, product, price FROM Products WHERE product_id = ?", result)
        productid = cart[0]['product_id']
        product = cart[0]['product']
        price = float(cart[0]['price'])
        quantity = 1
        totalprice = price * quantity

        # If cart empty insert product
        empty = db.execute("SELECT user_id FROM cart WHERE user_id NOT NULL AND user_id= ?", id)
        if len(empty) == 0:
            db.execute("INSERT INTO cart (user_id, product_id, product, price, quantity, totalprice) VALUES(?,?,?,?,?,?)",
            id, productid, product, format(price, '2f'), int(quantity), format(totalprice, '2f'))
            return result

        # If cart not empty check for product ID and update quantity else insert product
        if db.execute("SELECT user_id, product_id FROM cart WHERE user_id = ? AND product_id = ?", id, productid):
            db.execute("UPDATE cart SET quantity = quantity + 1 WHERE user_id = ? AND product_id = ?", id, productid)
            db.execute("UPDATE cart SET totalprice = price * quantity WHERE user_id = ? AND product_id = ?", id, productid)
            return result
        else: 
            db.execute("INSERT INTO cart (user_id, product_id, product, price, quantity, totalprice) VALUES(?,?,?,?,?,?)",
            id, productid, product, format(price, '2f'), int(quantity), format(totalprice, '2f'))
            return result


@app.route("/transactions", methods=["GET", "POST"])
@login_required
def transactions():
    """Show shopping cart"""

    id = session["user_id"]

    if request.method == "GET":

        # Obtain user name from users table
        firstname = db.execute("SELECT firstname from users WHERE id = ?", id)
        userfirstname = firstname[0]['firstname']

        # If no invoices render_template tranactions
        emptyinvoice = db.execute("SELECT user_id from invoices WHERE user_id = ? AND user_id NOT NULL", id)
        if len(emptyinvoice) == 0:
            return render_template("transactions.html", userfirstname=userfirstname)
        
        # Obtain sum(totalprice) from invoices table and format number
        totalprice1 = db.execute("SELECT sum(totalprice) FROM invoices WHERE user_id = ?", id)
        totalprice2 = totalprice1[0]['sum(totalprice)']
        totalprice3 = '{:,.2f}'.format(totalprice2)
        
        trans = db.execute("SELECT * FROM transactions WHERE user_id = ?", id)
        return render_template("transactions.html", userfirstname=userfirstname, trans=trans, totalprice=totalprice3)

    if request.method == "POST":

        #  Retrieve invoice number from button
        if request.form.get('invoice_no'):
            invno = request.form.get('invoice_no')

            # Collate invoice information and put into variables
            invinfo = db.execute("SELECT * FROM invoices WHERE user_id = ? and invoice_no = ?", id, invno)
            totpri = db.execute("SELECT totalprice, sqltime FROM transactions WHERE invoice_no = ?", invno )
            totalpri = totpri[0]['totalprice']
            sqltime = totpri[0]['sqltime']
            invdate = sqltime[:10]
            return render_template("invoices.html", invno=invno, invinfo=invinfo, totalprice=totalpri, invdate=invdate)


######################################################################################################

#Todo: 
    # about page
    # quantity indicator
    

#######################################################################################################


@app.route("/shopcart", methods=["GET", "POST"])
@login_required
def shopcart():
    """Show shopping cart"""

    id = session["user_id"]

    if request.method == "GET":
        
        # Return render_template("shopcart.html") to include user name
        firstname = db.execute("SELECT firstname from users WHERE id = ?", id)
        userfirstname = firstname[0]['firstname']
    
        # If no items in cart render shopcart.html unpopulated
        data = db.execute("SELECT * FROM cart WHERE user_id = ?", id)
        if len(data) == 0:
            return render_template("shopcart.html", carty="None", userfirstname=userfirstname, totalsum="0.00")
        
        # Select all information from cart 
        if db.execute("SELECT * FROM cart WHERE user_id = ?", id):
            carty = db.execute("SELECT * FROM cart WHERE user_id = ?", id)

            # If items in cart render shopcart.html with details
            if db.execute("SELECT * FROM cart WHERE user_id = ?", id):
                # Obtain sum(price) and convert to two decimal places
                cartdata = db.execute("SELECT * FROM cart WHERE user_id = ?", id)
                totalsum1 = db.execute("SELECT sum(totalprice) FROM cart WHERE user_id = ?", id)
                totalsum2 = totalsum1[0]['sum(totalprice)']
                totalsum = '{:,.2f}'.format(totalsum2)
                return render_template("shopcart.html", carty=cartdata, userfirstname=userfirstname, totalsum=totalsum)

    if request.method == "POST":

        # Button to remove all items from cart
        if request.form.get("removeall"):
            db.execute("DELETE FROM cart WHERE user_id = ?", id)
            flash("All items removed from shopping cart")
            return redirect("/shopcart")

        #  Button to remove items or reduce quantity
        if request.form.get('productitem'):
            prodid = request.form.get('productitem')
            prodid_ = db.execute("SELECT * FROM cart WHERE user_id = ? AND product_id = ?", id, prodid)
            pro_id = prodid_[0]['product_id']
            # If quantity > 1 reduce quantity by one, else remove item
            if db.execute("SELECT quantity FROM cart WHERE quantity > 1 AND user_id = ? AND product_id = ?", id, pro_id):
                db.execute("UPDATE cart SET quantity = quantity - 1 WHERE user_id = ? AND product_id = ?", id, pro_id)
                db.execute("UPDATE cart SET totalprice = price * quantity WHERE user_id = ? AND product_id = ?", id, pro_id)
            else:
                db.execute("DELETE FROM cart WHERE quantity = 1 AND user_id = ? AND product_id = ?", id, pro_id)
                
            # Remove items where items > quantity 1
            removeitems = db.execute("SELECT * FROM cart WHERE user_id = ?", id)
            
            # Flash and redirect if last item of last row removed
            if len(removeitems) == None and removeitems[0]['quantity'] == None:                
                db.execute("DELETE FROM cart WHERE user_id = ?", id)
                flash("All items removed from shopping cart")
                return redirect("/shopcart")

            # Collate information from databases to render template
            carty_ = db.execute("SELECT * FROM cart WHERE user_id = ?", id)
            userfirstname1_ = db.execute("SELECT firstname FROM users WHERE id = ?", id)
            userfirstname_ = userfirstname1_[0]['firstname']
            totalsum1_ = db.execute("SELECT sum(totalprice) FROM cart WHERE user_id = ?", id)
            
            if totalsum1_[0]['sum(totalprice)'] == None:
                flash("All items removed from shopping cart")
                return redirect("/shopcart")
           
            totalsum2_ = float(totalsum1_[0]['sum(totalprice)'])
            totalsum_ = '{:,.2f}'.format(totalsum2_)
            return render_template("shopcart.html", carty=carty_, userfirstname=userfirstname_, totalsum=totalsum_)

        if not request.form.get("pname"):
            return apology("must provide name", 400)
                
        if not request.form.get("pnumber") or len(request.form.get("pnumber")) < 4:
            return apology("must provide account number", 400)
               
        if not request.form.get("pexpiry"):
            return apology("must provide expiry date", 400)

        if not request.form.get("pcsv"):
            return apology("must provide csv number", 400)

        # Collate information from payment form
        pna = request.form.get("pname")
        pnu = request.form.get("pnumber")
        pnu4 = pnu[-4:]
        pex = request.form.get("pexpiry")
        pcs = request.form.get("pcsv")
        
        # Obtain sum(price) from cart
        if db.execute("SELECT * FROM cart WHERE product_id NOT NULL"):
            # Obtain sum(price) and convert to two decimal places
            sumprice = db.execute("SELECT sum(totalprice) FROM cart WHERE price NOT NULL and user_id = ?", id)
            sumprice2 = float(sumprice[0]['sum(totalprice)'])
            totalsum1 = '{:,.2f}'.format(sumprice2)

            # Insert information into transactions table
            db.execute("INSERT INTO transactions (user_id, totalprice, payname, paynumber, paynumber4, payexpiry, paycvs) VALUES(?,?,?,?,?,?,?)",
                id, totalsum1, pna, int(pnu), int(pnu4), pex, pcs)
            
            # Select highest invoice number as this will be the latest
            invoiceno = db.execute("SELECT max(invoice_no) FROM transactions WHERE user_id = ?", id)
            invoiceno_ = invoiceno[0]['max(invoice_no)']

            # Select all from shopping cart
            cartgrab = db.execute("SELECT * FROM cart WHERE user_id = ?", id)

            for row in cartgrab:
                productid_ = row['product_id']
                product_ = row['product']
                price_ = row['price']
                quantity_ = row['quantity']
                totalprice_ = price_ * quantity_
                
                db.execute("INSERT INTO invoices (user_id, invoice_no, product_id, product, price, quantity, totalprice) VALUES (?,?,?,?,?,?,?)",
                    id, invoiceno_, productid_, product_, price_, quantity_, totalprice_)

                # Delete all from cart after payment
                db.execute("DELETE FROM cart WHERE product IS NOT NULL and user_id = ?", id)
        flash("Thank you for your transaction")
        return redirect("/shopcart")           



@app.route("/about", methods=["GET"])
@login_required
def about():
    """about page"""

    if request.method == "GET":
        return render_template("about.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Clear user_id
    session.clear()

    # User reached route via Post (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure usernam was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
       
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



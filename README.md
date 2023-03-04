# Art Ghetto Collections Web Application
#### Video Demo:  <https://youtu.be/2cIkOAG4cJU>
#### Description:

Art Ghetto Collection is a web application designed to enable users to purchase pictures from a range of collections. It is an easy to navigate and straightforward shop providing registered users one or two click access to all pages. Users register and login much like they did for Finance and are directed to the homepage with links to View Art, Shopping Cart, About, and Account History.

View Art allows users to select and browse art collections with premium price tags. A user can click on buy buttons which will display quantity for two seconds and add item to cart. The Shopping Cart lists the selected items with product name, price, and quantity. Users can either remove or purchase the pictures. Cart will remain saved when a user logs out. Account History details all transactions made, with a link to select a breakdown of items purchased within that transaction.

My future endeavours are likely moving towards web development and so the obvious next step was to practise web applications. Using the framework Flask I wrote code in Python, SQL HTML, CSS, and Javascript. Included with these were Ajax and Jinja.

Using Finance as a model, which in all fairness changed considerably, I began with layout.html, before moving onto registration.html and login.html. As these are similar to Finance, I’ll be brief for this section. For layout.html I used a bootstrap navigation bar, which I restyled with CSS. Though I tinkered with the style throughout the process. I then used jinja to use this style for all other html files, as learned in pset9.

Creating register.html, I had to create a sqlite3 table called users. Here I asked users for first name, last name, username, password, confirm password, and email address. An error 400 page, similar to but not the same as Finance, was created for user input errors. I used a few nifty lines of html code to put a picture behind the image, and discarded Grumpy Cat, with emotional reluctance of course. I used a replace filter in Jinja to replace the hyphens that appear when not using the memegen.link and entered spaces. It did the trick!

This then directs users to the login page which would lookup users and password on the database. On successful login a user is directed to the home page (index.html), with a flash message and a greeting to the users first name, with the help of Jinga.

View Art was the biggest challenge, not least because I find Javascript and Ajax a little daunting. I was however committed to an idea I had. I wanted a dropdown menu where a user can select different Art Collections which appear without refreshing the page. I selected three sets of nine pictures for each collection (not to overdo it), styled in CSS to be the same size, bordered, and with a slight shadow for effect. All pictures are saved in the static folder. Incidentally these same pictures were used for the homepage and error page, manipulated in Microsoft Word, to appear miniature and scattered, and faded on the error page. A print screen was then saved as a jpeg in the static folder. I believe design to be an important element of web development so spent extra time on this.

With the help of David and Doug’s videos, and a little help from Stackoverflow, I developed a function in Javascript called ‘dropdownview’ which talks to view.html via calling the function with ‘onchange’ tag. The function works nicely. One snag though were the pictures on the initial page that move to the bottom of the page. I would prefer these to disappear but didn’t want to tamper with the code after it worked. However, it doesn’t look terrible.

The next challenge was a function to calculate the quantity and total price and add items to the shopping cart. The quantity function was surprisingly challenging! Such a simple idea we see everywhere and yet a major hinderance for me. I was hoping for a function to add quantity and add an item to cart on one click. However, I think I broke a coding rule by not developing a function that can iterate through all the buttons like ‘dropdownview’ did. I eventually cheated here by using 27 functions, one for each picture to do the job. It works, but not great design – I bare to think what would happen with 1000s of products. I had one other issue with the quantity. It pushes through to the database nicely but fails to calculate onscreen when moving between Art Collections. It’s not a disaster but I couldn’t find a workaround without tampering with the Javascript I’m not confident with. From here everything works smoothly.

To save the information in cart I created a table called ‘cart’. The cart is a temporary table. It keeps data until either removed by the user or purchased. The cart will remain if a user logs out and logs in. Each user has a unique id which appears in all tables. When a user clicks ‘Pay now’ items are inserted into two more tables: ‘transactions’ and ‘invoices’. Transactions save purchase information and invoices saves all items bought within that payment. Items purchased by user are then deleted from cart. By using user_id in cart enabled multiple users to use this cart.

Users can then click Account History to view all transactions and click on ‘see items’ to view the item breakdown for that transaction.

Users can then buy more or logout!


Folders and Files:

/project folder

app.py
The main python code includes the following imports:

from cs50 import SQL
from flask import Flask, json, redirect, render_template, request, session, flash
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required

helpers.py
Extra python functions supplied by Finance: login and apology – though grumpy cat has gone.

customer.db
Sqlite3 – includes five tables:
1.	users: id, username, userfirstname, userlastname, useremail, hash.
2.	products: product_id, product, price.
3.	cart: user_id, product_id, product, price, quantity, totalprice.
4.	transactions: invoice_no, user_id, totalprice, payname, paynumber paynumber4, payexpiry, paycvs, sqltime.
5.	invoices: user-id, invoice_no, product_id, product, price, quantity, totalprice, sqltime.

README.md
You’re looking at me!



/static folder

main.js
Javascript wouldn’t run from its own folder, so here it stayed.

favicon.io
Contains favicon of a camera downloaded for free from:
https://www.cleanpng.com/png-logo-drawing-clip-art-favicon-4360104/

jpegs
Includes 27 Art Collection pictures, home page picture, faded home page picture.

styles.css
No website is complete without css – I worked to create a slick, stylistic, premium look. I believe a good web developer should have a good eye for design.

html files - 
These three html files are used in conjunction with javascript, particularly the dropdown menu in view.html. I believe they simply needed to be in the same folder as main.js.

/templates folder

layout.html
register.html
login.html
apology.html
index.html
view.html
shopcart.html
transactions.html
invoice.html
about.html


Disclaimer: This is a fake web application with pictures selected from opensource website https://unsplash.com/. So, don’t buy them! Payment details are saved to the database. So don’t use real card details!



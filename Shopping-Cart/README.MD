PROJECT TITLE:
Electronics Web Apllication

Video Demo:
https://youtu.be/azFrUG_oQ48

#Description:

This project contains several files which having electronics application loading five random products
from data base into the electronics list and through this application you can add any kind of electronics
products into your electronics list and it's showing directely and also once you refresh the web page
the list of brands changed every time and also you can remove any product from electronics list
by click on it and tab the remove button it is very useful and fully functional.

######app.py:
Includes the backend of the application - all the routes and request logic for application.

In the begining we have our imports and we initialise a class for application we call it app.

Right below we define a secret key for our application and this key will be used to encrypt our cookies.

Right below we make made the configration to session into our app to run flask localy.

Right below we define the main route of our application with an index function,
we unpacking data into the session variable and we will wrap all items inside a set of square brackets
as a string so it's sort of the key and we do the same with the electronics items, and we do the same with
the render template.

Right below we define the add items route to our application with an add_items function,
we append our new item into the electronics list and we append also our request.form in the key of select items, and to make sessions work we specify some methods into the main route we go for post and get.

Right below we define the remove items route to our application with an remove_items function,
we want to select all the active checkbox input elements from HTML page, we type request.form.get list and inside these round brackets  we specify the name of our checkbox input elements (check)
after that we assign this expression to checked boxes, after that we made aloop for items into checked boxes and we also add conditional statement where if item in session in the key of the electronics item
only then we will remove this item and we will do this by popping it from electronics list and we assign this expression for idx after that we update our session.

Right below we have get our database function which is basically connecting our sqlite database,
and we have already established a connection with our database and we call this connection DB,
after that we created cursor object and we can use this cursor object to execute SQL commands,
under these we type cursor.execute and inside the round brackets we pass an SQL command of
select row of name from electronics which is the name of the table inside the electronics list database,
we made all data into the electronics list nad we use random shuffle function to showing 5 product every time, uder these we made return for all data of electronics list which represent the result of our execute command.

Right below we add these blocks of codes they are responsible for terminating our database
connection once we are done using it.

lastly if name equal main then our app will run.

#Electronics.db:
a complete SQLite electronics database which was created with Electronics.py including list of electronics products like :
apple nokia sony LG and etc....

#Electronics.py:
the file which created Electronics.db including the list of all eclectronic products,
we assign this experssion to list and also sorted, we made the connection with the database after that
we assign this expression to cursor and we created a table of electronics list including the row id which is the primary key and the row name, after that we made aloop to add all items into the table.


##Templates/index.html:
The HTML template of the application, we made atitle of the page to Electronics, after that we add the link for styelsheet file css and the link for javascript file.

inside the body we add a header including statement of Electronics.

after that we created acontanair including a form add item with method post and we add some placeholders for all our items using jinja inside we made aloop for item in all data, and we place item as a text inside it and we specify the item in a set of curly brackets after that we ending the for loop, after that we add input with name ADD ITEM with id add_btn.

##static/css/main.css:
The stylesheet of the application including all styling tags of application.

we made ageneral styling to the page body by selecting the font-family : raleway, font-size: 1.5em, text-align: center.

after that i add some margin around the electronics list labels by sit their margin to 25px for the top and bottom as well as 5px for the left and right.

we made also style to our entire electronics list by adding to the div container remove items background color:thistle, color: darkslategrey,
padding: 30px.

after that we made style for add_btn by selecting background-color: hotpink, color: floralwhite, font-weight: bold, border-radius: 20px,border: 2px solid white, margin: 10px; padding: 10px 15px, cursor: pointer,

after that we made style for remove_btn by selecting the background-color: gainsboro, color: black, font-weight: bold,border-radius: 20px, border: 2px solid white, margin: 10px,
padding: 10px 15px,

after that we made styling for select tag by add font-family: raleway,
font-size: 0.85em, text-align: center, width: 200px, margin: 50px 10px,
padding: 5px 0, border: 2px solid darkgray,

lastly we made style for hover by selecting background-color: darkred.

##static/js/main.js:
includes all the client side interactions of the application.

first we add a callback function to our checkbox elements.

we will begin after that by defining our checkme function and this function receives some input so we will create a parameter inside hold input id.

we did this by opening square brackets document.queryselector and inside the round brackets we specify the input field with id of input id which we simply concatenate + input id and we also closed the square brackets,
and we assign this expression to a variable var hold checked input.

we did the similar to our labels.

after that we did some changes to these items, if checked input.checked then we set a text decoration to our checked label by line-through and other wise if uncheck this element the text decoration will also disappear.

after that we made changes to our button by document.getelement by id which we passed the id of remove btn and we assign this expression to a variable name called btn.

after that we we add btn.value to set the inner text to our button to remove items, then we set the font color to"#FFFFFF";
backgroundColor to "#FE7575"; cursor = "pointer";
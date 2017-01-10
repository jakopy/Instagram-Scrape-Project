==================
Requirements
=================
<b>Python v 2.7</b></br>
Modules: </br>
<ul>
<li><a href="http://flask.pocoo.org/">Flask</a></li>
<li><a href="http://jinja.pocoo.org/">Jinja2</a></li> 
<li><a href="https://docs.python.org/2/library/sqlite3.html">Sqlite3</a></li>
</ul>

=====================
View The Application
====================
<b>Steps</b></br>
1. Run python app.py in the command prompt</br>
2. Go to any browser and type in http://127.0.0.1:5000/instagram_search</br>
3. Type in a for the Search Term, 0 for min followers, 100000000000 for max followers then click submit</br>
4. Once the submit button is clicked, you can view an instagram profile by clicking on the blue text</br>

==============
How This Application Works
=============
The app is created with flask. </br>
Urls are created starting with localhost with a path </br>
When a user goes to the proper url, Flask listens for when the user enters in the fields and then clicks the submit button </br>
When the user clicks the submit button flask renders a webpage via jinja </br>
The data that is rendered through jinja comes from a sqlite database located in the data folder

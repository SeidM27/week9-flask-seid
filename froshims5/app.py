# Stores registrants in a SQLite database

# TODO: Import SQL from cs50
# TODO: Import Flask, redirect, render_template, and request from flask


# TODO: Create the Flask app instance


# TODO: Connect to the SQLite database "froshims.db" using cs50's SQL()
#       and store it in a variable called db


# TODO: Define the SPORTS list with at least 3 sport names


# TODO: Define a GET route for "/" that renders index.html with sports=SPORTS


# TODO: Define a POST route for "/register" that:
#         1. Validates name (missing → error.html with message="Missing name")
#         2. Validates sport (missing → "Missing sport", not in SPORTS → "Invalid sport")
#         3. Inserts the registrant into the database:
#            db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)
#         4. Redirects to "/registrants"


# TODO: Define a GET route for "/registrants" that:
#         - Queries all rows from the registrants table
#         - Renders registrants.html passing the results as "registrants"
from cs50 import SQL
from flask import Flask, redirect, render_template, request
app = Flask(__name__)
SPORTS = ["Basketball", "Football", "Volleyball", "Tennis"]
@app.route("/")
def index():
return render_template("index.html", sports=SPORTS)
@app.route("/register", methods=["POST"])
def register():
name = request.form.get("name")
sport = request.form.get("sport")
if not name or sport not in SPORTS:
return render_template("failure.html")
db.execute("INSERT INTO registrants (name, sport) VALUES (?, ?)", name, sport)
return redirect("/registrants")
@app.route("/registrants")
def registrants():
rows = db.execute("SELECT * FROM registrants")
return render_template("registrants.html", registrants=rows)
{% block body %}
<h1>Registrants</h1>
<table>
<tr><th>Name</th><th>Sport</th></tr>
{% for row in registrants %}
<tr>
<td>{{ row["name"] }}</td>
<td>{{ row["sport"] }}</td>
</tr>
{% endfor %}
</table>
{% endblock %}


# Implements a registration form using a select menu, validating sport server-side

# TODO: Import Flask, render_template, and request from the flask package


# TODO: Create the Flask app instance


# TODO: Define a SPORTS list containing at least 3 sport names


# TODO: Define a GET route for "/" that renders index.html
#       Pass the SPORTS list to the template as the variable "sports"


# TODO: Define a POST route for "/register" that:
#         - Reads "name" from the form
#         - Reads "sport" from the form
#         - If name is missing OR sport is not in the SPORTS list → render failure.html
#         - Otherwise → render success.html
from flask import Flask, render_template, request
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
return render_template("success.html")
{% block body %}
<h1>Register</h1>
<form action="/register" method="post">
<input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
<select name="sport">
<option value="">Sport</option>
{% for sport in sports %}
<option value="{{ sport }}">{{ sport }}</option>
{% endfor %}
</select>
<button type="submit">Register</button>
</form>
{% endblock %}


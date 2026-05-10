# Adds error messages

# TODO: Import Flask, render_template, and request from flask


# TODO: Create the Flask app instance


# TODO: Define the SPORTS list with at least 3 sport names


# TODO: Define a GET route for "/" that renders index.html with sports=SPORTS


# TODO: Define a POST route for "/register" that validates step by step:
#         1. Get "name" — if missing, render error.html with message="Missing name"
#         2. Get "sport" — if missing, render error.html with message="Missing sport"
#         3. If sport is not in SPORTS, render error.html with message="Invalid sport"
#         4. If all valid, render success.html
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
if not name:
return render_template("error.html", message="Missing name")
if sport not in SPORTS:
return render_template("error.html", message="Invalid sport")
return render_template("success.html")

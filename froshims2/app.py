# Implements a registration form using radio buttons

from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():

    # Validate submission
    if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        return render_template("failure.html")

    # Confirm registration
    return render_template("success.html")
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
{% for sport in sports %}
<input name="sport" type="radio" value="{{ sport }}"> {{ sport }}
{% endfor %}
<button type="submit">Register</button>
</form>
{% endblock %}

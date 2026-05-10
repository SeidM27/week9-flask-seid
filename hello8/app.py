# Switches to POST

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greet", methods=["POST"])
def greet():
    return render_template("greet.html", name=request.form.get("name", "world"))
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def index():
return render_template("index.html")
@app.route("/greet", methods=["POST"])
def greet():
name = request.form.get("name", "world")
return render_template("greet.html", name=name)
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Flask Exercise</title>
</head>
<body>
{% block body %}{% endblock %}
</body>
</html>
             {% block body %}
<form action="/greet" method="post">
<input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
<button type="submit">Greet</button>
</form>
{% endblock %}
{% block body %}

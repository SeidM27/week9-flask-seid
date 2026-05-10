# Adds a layout

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greet")
def greet():
    return render_template("greet.html", name=request.args.get("name", "world"))
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def index():
return render_template("index.html")
@app.route("/greet")
def greet():
name = request.args.get("name", "world")
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

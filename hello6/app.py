# Adds a form, second route

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greet")
def greet():
    return render_template("greet.html", name=request.args.get("name", "world"))
    ello6/app.py
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
<head><title>Hello</title></head>
<body>
<form action="/greet" method="get">
<input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
<button type="submit">Greet</button>
</form>
</body>
</html>
hello6/templates/greet.html
<!DOCTYPE html>
<html lang="en">
<head><title>Greet</title></head>
<body>
<h1>hello, {{ name }}</h1>
</body>
</html>


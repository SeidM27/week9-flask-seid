# Moves default value to template

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("greet.html", name=request.form.get("name"))
    return render_template("index.html")
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
if request.method == "POST":
return render_template("greet.html", name=request.form.get("name"))
return render_template("index.html")
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Flask Exercise</title>
</head>
<body>
{% block body %}{% endblock %}
</body>
</html>{% block body %}
<form action="/" method="post">
<input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
<button type="submit">Greet</button>
</form>
{% endblock %}

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "Bigman-1234"

@app.route("/hello")
def index():
    flash("what's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", nice to see you!")
    return render_template("index.html")
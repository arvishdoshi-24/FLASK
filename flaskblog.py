from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>HOME PAGE</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"
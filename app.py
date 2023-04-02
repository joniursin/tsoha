from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute(text("SELECT name FROM restaurants"))
    restaurants = result.fetchall()
    return render_template("index.html", count=len(restaurants), restaurants=restaurants)

@app.route("/review/<int:id>")
def review(id):
    return render_template("review.html")

@app.route("/view/<int:id>")
def view(id):
    return render_template("view.html")

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
    sql = "SELECT id, name FROM restaurants"
    result = db.session.execute(text(sql))
    restaurants = result.fetchall()
    return render_template("index.html", count=len(restaurants), restaurants=restaurants)

@app.route("/review/<int:id>")
def review(id):
    sql = "SELECT name FROM restaurants WHERE id=:id"
    result = db.session.execute(text(sql), {"id":id})
    restaurant = result.fetchone()
    return render_template("review.html", id=id, restaurant=restaurant)

@app.route("/add_review", methods=["POST"])
def add_review():
    rating_id = request.form["id"]
    rating = request.form["rating"]
    message = request.form["message"]
    sql = "INSERT INTO reviews (restaurant_id, user_id, rating, content, created_at) VALUES (:rating_id, 1, :rating, :message, NOW())"
    db.session.execute(text(sql), {"rating_id":rating_id, "rating":rating, "message":message})
    db.session.commit()
    return redirect("/view/" + str(rating_id))
    

@app.route("/view/<int:id>")
def view(id):
    sql = "SELECT name FROM restaurants WHERE id=:id"
    result = db.session.execute(text(sql), {"id":id})
    restaurant = result.fetchone()
    
    sql = "SELECT rating, content, created_at FROM reviews WHERE restaurant_id=:id"
    result = db.session.execute(text(sql), {"id":id})
    reviews = result.fetchall()
    return render_template("view.html", reviews=reviews, restaurant=restaurant)

from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

import authentication
import like

def admin_status():
    sql = "SELECT op_status FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":session["username"]})
    op_status = result.fetchone()
    if op_status[0]:
        return True
    return False

@app.route("/")
def index():
    sql = "SELECT id, name FROM restaurants"
    result = db.session.execute(text(sql))
    restaurants = result.fetchall()
    return render_template("index.html", count=len(restaurants), restaurants=restaurants, admin_status=admin_status)

@app.route("/review/<int:id>")
def review(id):
    sql = "SELECT name FROM restaurants WHERE id=:id"
    result = db.session.execute(text(sql), {"id":id})
    restaurant = result.fetchone()
    return render_template("review.html", id=id, restaurant=restaurant)

@app.route("/add_review", methods=["POST"])
def add_review():
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":session["username"]})
    user_id = result.fetchone()
    try:
        rating_id = request.form["id"]
        rating = request.form["rating"]
        message = request.form["message"]
    except:
        return render_template("error.html", error="Virheellinen arvostelu jätä ainakin arvosana!")
    
    sql = "INSERT INTO reviews (restaurant_id, user_id, username, rating, content, created_at, visible) VALUES (:rating_id, :user_id, :username, :rating, :message, NOW(), True)"
    db.session.execute(text(sql), {"rating_id":rating_id, "user_id":user_id.id, "username":session["username"], "rating":rating, "message":message})
    db.session.commit()
    return redirect("/view/" + str(rating_id))
    

@app.route("/view/<int:id>")
def view(id):
    sql = "SELECT name FROM restaurants WHERE id=:id"
    result = db.session.execute(text(sql), {"id":id})
    restaurant = result.fetchone()

    sql = "SELECT id, op_status FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":session["username"]})
    user = result.fetchone()

    sql = "SELECT r.id, r.username, r.rating, r.content, r.created_at, r.visible, COUNT(l.id) FROM reviews r LEFT JOIN likes l ON r.id=l.review_id WHERE restaurant_id=:id GROUP BY r.id, r.username, r.rating, r.content, r.created_at, r.visible ORDER BY COUNT(l.id) DESC" #change username to just id and search with that
    result = db.session.execute(text(sql), {"id":id})
    reviews = result.fetchall()

    return render_template("view.html", reviews=reviews, restaurant=restaurant, op_status=user[1], user_id=user[0], has_liked=like.has_liked, get_likes=like.get_likes)
    #return render_template("view.html", reviews=reviews, restaurant=restaurant, op_status=True) #debug

@app.route("/remove", methods=["POST"])
def remove():
    id = request.form["id"]
    sql = "UPDATE reviews SET visible = false WHERE id=:id"
    db.session.execute(text(sql), {"id":id})
    db.session.commit()

    return redirect("/")

@app.route("/new_restaurant")
def new_restaurant():
    return render_template("new-restaurant.html", admin_status=admin_status)

@app.route("/add_restaurant", methods=["POST"])
def add_restaurant():
    name = request.form["name"]
    sql = "INSERT INTO restaurants (name) VALUES (:name)"
    db.session.execute(text(sql), {"name":name})
    db.session.commit()
    return redirect("/")

@app.route("/new_group")
def new_group():
    sql = "SELECT id, name FROM restaurants"
    result = db.session.execute(text(sql))
    restaurants = result.fetchall()
    return render_template("new-group.html", admin_status=admin_status, restaurants=restaurants)

@app.route("/add_group", methods=["POST"])
def add_group():
    try:
        group_name = request.form["name"]
    except:
        return render_template("error.html", error="Nimeä ryhmälle ei annettu!")
    
    chosen_restaurants = request.form.getlist("restaurant_id")

    sql = "INSERT INTO groups (group_name) VALUES (:group_name) RETURNING id"
    group_id = db.session.execute(text(sql), {"group_name":group_name}).fetchone()[0]

    for i in chosen_restaurants:
        sql = "INSERT INTO group_members (group_id, restaurant_id) VALUES (:group_id, :restaurant_id)"
        db.session.execute(text(sql), {"group_id":group_id, "restaurant_id":int(i)})

    db.session.commit()
    return redirect("/")


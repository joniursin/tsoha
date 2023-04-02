from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    sql = "SELECT id, name FROM restaurants"
    result = db.session.execute(text(sql))
    restaurants = result.fetchall()
    return render_template("index.html", count=len(restaurants), restaurants=restaurants)

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/add_user", methods=["POST"])
def add_user():
    username = request.form["username"]
    password = request.form["password"]

    hash_value = generate_password_hash(password)
    sql = "INSERT INTO users (username, password, op_status) VALUES (:username, :password, FALSE)"
    db.session.execute(text(sql), {"username":username, "password":hash_value})
    db.session.commit()
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":username})
    user = result.fetchone()    
    if not user:
        return render_template("error.html", error="Invalid username")
    else:
        hash_value = user.password
    if check_password_hash(hash_value, password):
        session["username"] = username
    else:
        return render_template("error.html", error="Invalid password")
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

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

from app import app, db, admin_status
from flask import Flask
from flask import redirect, render_template, request, session, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

@app.route("/new_group")
def new_group():
    sql = "SELECT id, name FROM restaurants"
    result = db.session.execute(text(sql))
    restaurants = result.fetchall()
    return render_template("new-group.html", admin_status=admin_status, restaurants=restaurants)

@app.route("/add_group", methods=["POST"])
def add_group():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    group_name = request.form["name"]
    if group_name == "":
        return render_template("error.html", error="Nimeä ryhmälle ei annettu!")
    
    chosen_restaurants = request.form.getlist("restaurant_id")

    sql = "INSERT INTO groups (group_name) VALUES (:group_name) RETURNING id"
    group_id = db.session.execute(text(sql), {"group_name":group_name}).fetchone()[0]

    for i in chosen_restaurants:
        sql = "INSERT INTO group_members (group_id, restaurant_id) VALUES (:group_id, :restaurant_id)"
        db.session.execute(text(sql), {"group_id":group_id, "restaurant_id":int(i)})

    db.session.commit()
    return redirect("/")
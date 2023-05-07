from flask import redirect, render_template, request, session, abort
from sqlalchemy.sql import text
from app import app, db, admin_status

@app.route("/new_group")
def new_group():
    sql = "SELECT id, name FROM restaurants WHERE visible=true"
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

    if not chosen_restaurants:
        return render_template("error.html", error="Valitse ainakin yksi ravintola ryhmään!")

    sql = "INSERT INTO groups (group_name) VALUES (:group_name) RETURNING id"
    group_id = db.session.execute(text(sql), {"group_name":group_name}).fetchone()[0]

    for i in chosen_restaurants:
        sql = "INSERT INTO group_members (group_id, restaurant_id) VALUES (:group_id, :restaurant_id)"
        db.session.execute(text(sql), {"group_id":group_id, "restaurant_id":int(i)})

    db.session.commit()
    return redirect("/")

@app.route("/groups")
def groups():
    sql = "SELECT id, group_name FROM groups"
    result = db.session.execute(text(sql))
    groups = result.fetchall()
    return render_template("groups.html", count=len(groups), groups=groups, admin_status=admin_status)

@app.route("/view_group/<int:id>")
def view_group(id):
    sql = "SELECT group_name FROM groups WHERE id=:id"
    result = db.session.execute(text(sql), {"id":id})
    group_name = result.fetchone()[0]

    sql = "SELECT r.id, r.name FROM group_members g JOIN restaurants r ON g.restaurant_id=r.id WHERE group_id=:id AND r.visible=true"
    result = db.session.execute(text(sql), {"id":id})
    restaurants = result.fetchall()
    return render_template("view-group.html", id=id, restaurants=restaurants, group_name=group_name)

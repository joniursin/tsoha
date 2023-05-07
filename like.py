from flask import redirect, request, session, abort
from sqlalchemy.sql import text
from app import app, db

def has_liked(review_id, user_id):
    sql = "SELECT review_id FROM likes WHERE review_id=:review_id AND user_id=:user_id"
    result = db.session.execute(text(sql), {"review_id":review_id, "user_id":user_id})
    like_status = result.fetchone()
    if like_status is None:
        return False
    return True

def get_likes(review_id):
    sql = "SELECT COUNT(*) FROM likes WHERE review_id=:review_id"
    result = db.session.execute(text(sql), {"review_id":review_id})
    return result.fetchone()[0]

@app.route("/like", methods=["POST"])
def like():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    review_id = request.form["review_id"]
    user_id = request.form["user_id"]
    restaurant_name = request.form["restaurant_name"]

    sql = "INSERT INTO likes (review_id, user_id) VALUES (:review_id, :user_id)"
    db.session.execute(text(sql), {"review_id":review_id, "user_id":user_id})
    db.session.commit()

    sql = "SELECT id FROM restaurants WHERE name=:restaurant_name"
    result = db.session.execute(text(sql), {"restaurant_name":restaurant_name})
    restaurant_id = result.fetchone()[0]

    return redirect("/view/" + str(restaurant_id))

@app.route("/remove_like", methods=["POST"])
def remove_like():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    review_id = request.form["review_id"]
    user_id = request.form["user_id"]
    restaurant_name = request.form["restaurant_name"]

    sql = "DELETE FROM likes WHERE review_id=:review_id AND user_id=:user_id"
    db.session.execute(text(sql), {"review_id":review_id, "user_id":user_id})
    db.session.commit()

    sql = "SELECT id FROM restaurants WHERE name=:restaurant_name"
    result = db.session.execute(text(sql), {"restaurant_name":restaurant_name})
    restaurant_id = result.fetchone()[0]

    return redirect("/view/" + str(restaurant_id))

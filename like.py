from app import app, db
from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

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
    review_id = request.form["review_id"]
    user_id = request.form["user_id"]

    sql = "INSERT INTO likes (review_id, user_id) VALUES (:review_id, :user_id)"
    db.session.execute(text(sql), {"review_id":review_id, "user_id":user_id})
    db.session.commit()
    print("tykätty")
    return redirect("/")

@app.route("/remove_like", methods=["POST"])
def remove_like():
    review_id = request.form["review_id"]
    user_id = request.form["user_id"]

    sql = "DELETE FROM likes WHERE review_id=:review_id AND user_id=:user_id"
    db.session.execute(text(sql), {"review_id":review_id, "user_id":user_id})
    db.session.commit()
    print("poistettu tykkäys")
    return redirect("/")
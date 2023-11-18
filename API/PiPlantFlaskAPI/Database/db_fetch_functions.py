import sqlite3
from sqlite3 import Error

import bcrypt
import jwt
from flask import jsonify, abort

import app
from Database.db_setup import getConnection


def fetchUsers():
    connection = getConnection()
    try:
        cur = connection.cursor()

        users = cur.execute("SELECT * FROM users;").fetchall()

        connection.commit()

        return jsonify(users)
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()


def login(loginUsername: str, loginPassword: str):
    connection = getConnection()
    try:
        user = connection.execute("SELECT * FROM users WHERE username = ?;", (loginUsername,)).fetchone()
        connection.commit()
        if user is None:
            abort(401)

        if not bcrypt.checkpw(loginPassword.encode(), user[2]):
            return jsonify(), 401

        if user:
            try:
                # token should expire after 24 hrs
                token = jwt.encode(
                    {"user_id": user["_id"]},
                    app.app.config["SECRET_KEY"],
                    algorithm="HS256"
                )
                return token
            except Exception as e:
                return {
                    "error": "Something went wrong",
                    "message": str(e)
                }, 422
        return {
            "message": "Error fetching auth token!, invalid email or password",
            "data": None,
            "error": "Unauthorized"
        }, 404

    except Error as e:
        print(f"Error in login func : {e}")
        abort(400)
    finally:
        if connection:
            connection.close()

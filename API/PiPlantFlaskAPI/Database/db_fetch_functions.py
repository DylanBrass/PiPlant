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

        for user in users:
            print(user)

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
        print(user)
        if user is None:
            abort(401)
        if not bcrypt.checkpw(loginPassword.encode(), user[2]):
            abort(401)

        print("user is not none")
        if user:
            try:
                token = jwt.encode(
                    {"user_id": user[0],
                     "exp": app.datetime.datetime.utcnow() + app.datetime.timedelta(minutes=15)},
                    app.app.config["SECRET_KEY"],
                    algorithm="HS256"
                )

                print(token)
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


def get_by_id(user_id):
    connection = getConnection()
    try:
        cur = connection.cursor()

        user = cur.execute("SELECT * FROM users WHERE id = ?;", (user_id,)).fetchone()

        connection.commit()

        return user
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

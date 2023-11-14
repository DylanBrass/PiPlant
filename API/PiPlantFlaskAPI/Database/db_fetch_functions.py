import sqlite3
from sqlite3 import Error

import bcrypt
from flask import jsonify, abort
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
        cur = connection.cursor()
        users = cur.execute("SELECT * FROM users WHERE username = ? AND password = ?;",
                            (loginUsername, bcrypt.hashpw(loginPassword.encode(), bcrypt.gensalt()))).fetchone()
        connection.commit()

        if users is None:
            abort(401)

        return jsonify(users)
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

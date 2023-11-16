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
    print(loginUsername)
    print(loginPassword)
    connection = getConnection()
    try:
        users = connection.execute("SELECT * FROM users WHERE username = ?;",
                                   loginUsername).fetchone()
        connection.commit()

        print(f"users : {users}")
        if users is None:
            abort(401)

        if bcrypt.checkpw(loginPassword.encode(), users[2]):
            return jsonify(users)

        abort(401)
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

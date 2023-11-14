import sqlite3
from sqlite3 import Error
from flask import jsonify
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

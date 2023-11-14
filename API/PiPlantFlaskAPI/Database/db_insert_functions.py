from sqlite3 import Error
import bcrypt
from flask import jsonify

from Database.db_setup import getConnection


def createUser(username: str, password: str):
    connection = getConnection()
    try:
        cur = connection.cursor()

        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                    (username, bcrypt.hashpw(password.encode(), bcrypt.gensalt()))
                    )
        connection.commit()

        return jsonify(), 201
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

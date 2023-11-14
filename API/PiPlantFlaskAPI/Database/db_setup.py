import sqlite3
from sqlite3 import Error

import bcrypt


def getConnection():
    return sqlite3.connect('UserPool.db')


def setUpDatabase():
    connection = getConnection()

    try:

        with open('../schema.sql') as f:
            connection.executescript(f.read())

        cur = connection.cursor()

        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                    ('TestUser', bcrypt.hashpw(b'pwd', bcrypt.gensalt()))
                    )

        connection.commit()
        connection.close()
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

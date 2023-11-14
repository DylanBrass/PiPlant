import sqlite3
from sqlite3 import Error


def fetchUsers():
    connection = sqlite3.connect('UserPool.db')
    try:
        cur = connection.cursor()

        users = cur.execute("SELECT * FROM users ;").fetchall()

        connection.commit()

        return users
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

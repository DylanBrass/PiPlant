import sqlite3
import bcrypt


def setUpDatabase():
    connection = sqlite3.connect('UserPool.db')

    with open('schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                ('TestUser', bcrypt.hashpw(b'pwd', bcrypt.gensalt()))
                )

    connection.commit()
    connection.close()

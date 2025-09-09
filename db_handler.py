import sqlite3


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='card';")
    result = cursor.fetchone()

    if not result:
        cursor.execute("""CREATE TABLE card(
            id INTEGER,
            number TEXT,
            pin TEXT,
            balance INTEGER DEFAULT 0);""")
        connection.commit()

    cursor.close()


def connection_maker():
    con = sqlite3.connect("card.s3db")
    create_tables(con)
    return con

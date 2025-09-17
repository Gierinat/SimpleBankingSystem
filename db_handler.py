import sqlite3


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='card';")
    result = cursor.fetchone()

    if not result:
        cursor.execute("""CREATE TABLE card(
            id INTEGER PRIMARY KEY,
            number TEXT,
            pin TEXT,
            balance INTEGER DEFAULT 0);""")
        connection.commit()

    cursor.close()


def connection_maker():
    con = sqlite3.connect("card.s3db")
    create_tables(con)
    return con


def save_card(connection, card):
    card_details = (card.card_number, card.pin)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO card(number, pin) VALUES (?, ?)", card_details)
    connection.commit()
    cursor.close()


def update_card(connection, card):
    card_details = (card.balance, card.card_number, card.pin)
    cursor = connection.cursor()
    cursor.execute("UPDATE card SET balance = ? WHERE number = ? AND pin = ?", card_details)
    connection.commit()
    cursor.close()


def get_card_details_by_number_pin(con, num, pin):
    card_details = (num, pin)
    cursor = con.cursor()
    cursor.execute("""SELECT number, pin, balance
                    FROM card
                    WHERE number = ?
                    AND pin = ?""", card_details)
    card_db = cursor.fetchone()
    return card_db


def check_card_exists(con, num):
    card_details = (num,)
    cursor = con.cursor()
    cursor.execute("""SELECT number, pin, balance
                    FROM card
                    WHERE number = ?""", card_details)
    card_db = cursor.fetchone()
    if card_db:
        return True
    else:
        return False

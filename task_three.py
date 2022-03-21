import sqlite3


CARDS = [
        ('0338100000521000100', '448400.00'),
        ('0338100000521000099', '80500.00'),
        ('0161100008221000004', '35000.00'),
        ('0347000000121000054', '125051.45'),
        ('32110590678 ', '21109928.54'),
        ('32110750824', '5629302.00'),
        ('0347000000121000053', '144913.80'),
        ('0161100008221000003', '580000.00'),
    ]


def createTable(table=CARDS):
    conn = sqlite3.connect(r'cards.db')
    cur = conn.cursor()
    cur.execute("""DROP TABLE IF EXISTS cards""")
    cur.execute("""CREATE TABLE cards(
       number INT,
       amount DOUBLE)
    """)
    conn.commit()

    cur.executemany("INSERT INTO cards VALUES(?, ?);", table)
    conn.commit()

    cur.execute("SELECT * FROM cards;")
    return cur


import sqlite3

db = sqlite3.connect("xj.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tg_id INTEGER UNIQUE,
    full_name TEXT,
    xj_id TEXT UNIQUE,
    qualification TEXT,
    phone TEXT,
    address TEXT,
    gift_number INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS settings(
    id INTEGER PRIMARY KEY,
    gift_limit INTEGER DEFAULT 50
)
""")

cursor.execute("""
INSERT OR IGNORE INTO settings(id, gift_limit)
VALUES(1,50)
""")

db.commit()


def check_user(tg_id):
    cursor.execute(
        "SELECT * FROM users WHERE tg_id=?",
        (tg_id,)
    )
    return cursor.fetchone()


def check_xj_id(xj_id):
    cursor.execute(
        "SELECT * FROM users WHERE xj_id=?",
        (xj_id,)
    )
    return cursor.fetchone()


def get_count():
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]


def get_limit():
    cursor.execute(
        "SELECT gift_limit FROM settings WHERE id=1"
    )
    return cursor.fetchone()[0]


def set_limit(limit):
    cursor.execute(
        "UPDATE settings SET gift_limit=? WHERE id=1",
        (limit,)
    )
    db.commit()


def add_limit(count):
    current = get_limit()

    cursor.execute(
        "UPDATE settings SET gift_limit=? WHERE id=1",
        (current + count,)
    )

    db.commit()


def add_user(
        tg_id,
        full_name,
        xj_id,
        qualification,
        phone,
        address,
        gift_number
):

    cursor.execute("""
    INSERT INTO users(
        tg_id,
        full_name,
        xj_id,
        qualification,
        phone,
        address,
        gift_number
    )
    VALUES(?,?,?,?,?,?,?)
    """, (
        tg_id,
        full_name,
        xj_id,
        qualification,
        phone,
        address,
        gift_number
    ))

    db.commit()

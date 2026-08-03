import sqlite3

db = sqlite3.connect("users.db", check_same_thread=False)
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    full_name TEXT,
    username TEXT,
    vip INTEGER DEFAULT 0,
    free_signals INTEGER DEFAULT 3
)
""")

db.commit()


def add_user(user_id, full_name, username):
    cursor.execute(
        "INSERT OR IGNORE INTO users(user_id, full_name, username) VALUES(?,?,?)",
        (user_id, full_name, username)
    )
    db.commit()


def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    return cursor.fetchone()


def set_vip(user_id):
    cursor.execute("UPDATE users SET vip=1 WHERE user_id=?", (user_id,))
    db.commit()


def use_free_signal(user_id):
    cursor.execute(
        "UPDATE users SET free_signals=free_signals-1 WHERE user_id=? AND free_signals>0",
        (user_id,)
    )
    db.commit()

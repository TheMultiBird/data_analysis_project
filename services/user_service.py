from db.db_utils import with_db_connection

@with_db_connection
def add_user(conn, name, email):
    conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))

@with_db_connection
def get_all_users(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    return cur.fetchall()

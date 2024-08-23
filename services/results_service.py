from db.db_utils import with_db_connection

@with_db_connection
def add_result(conn, user_id, score):
    conn.execute("INSERT INTO results (user_id, score) VALUES (?, ?)", (user_id, score))

@with_db_connection
def get_all_results(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM results")
    return cur.fetchall()

from db.db_utils import with_db_connection

@with_db_connection
def calculate_average_score(conn):
    cur = conn.cursor()
    cur.execute("SELECT AVG(score) FROM results")
    average_score = cur.fetchone()[0]
    if average_score:
        print(f"The average score is: {average_score:.2f}")
    else:
        print("No scores found.")

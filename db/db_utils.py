import sqlite3
from sqlite3 import Error
import os


def create_connection():
    """Create and return a database connection, ensuring the db directory exists."""
    db_path = "./db/database.sqlite"
    db_dir = os.path.dirname(db_path)

    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    try:
        conn = sqlite3.connect(db_path)
        return conn
    except Error as e:
        print(e)
    return None


def execute_sql(conn, sql, data=None):
    """Execute SQL with optional data; commit changes."""
    try:
        cur = conn.cursor()
        if data:
            cur.execute(sql, data)
        else:
            cur.execute(sql)
        conn.commit()
    except Error as e:
        print(e)


def with_db_connection(func):
    """Higher-order function to manage database connections."""
    def inner_function(*args, **kwargs):
        conn = create_connection()
        if conn:
            try:
                result = func(conn, *args, **kwargs)
                return result
            finally:
                conn.close()
        else:
            print("Failed to create a database connection.")
    return inner_function

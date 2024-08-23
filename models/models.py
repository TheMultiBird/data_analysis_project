create_users_table_sql = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
"""

create_results_table_sql = """
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    score INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

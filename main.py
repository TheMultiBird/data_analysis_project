from db.db_utils import create_connection, execute_sql
from models.models import create_users_table_sql, create_results_table_sql
from services.user_service import add_user, get_all_users
from services.results_service import add_result, get_all_results
from analysis.data_analysis import calculate_average_score

def setup_database():
    conn = create_connection()
    if conn is not None:
        execute_sql(conn, create_users_table_sql)
        execute_sql(conn, create_results_table_sql)
        conn.close()

def main():
    setup_database()

    # Sample data
    add_user("Alice Wonderland", "alice@example.com")
    add_user("Bob Builder", "bob@example.com")

    add_result(1, 90)
    add_result(2, 85)

    print("Users:", get_all_users())
    print("Results:", get_all_results())

    calculate_average_score()

if __name__ == "__main__":
    main()

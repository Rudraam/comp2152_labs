import sqlite3
from contextlib import closing

try:
    with closing(sqlite3.connect('test.db')) as db_conn:
        db_conn.row_factory = sqlite3.Row
        with closing(db_conn.cursor()) as cursor:
            try:
                query_1 = "SELECT * FROM demo WHERE id > 14"
                cursor.execute(query_1)
                rows = cursor.fetchall()
                print("Name of rows with id > 14")
                for row in rows:
                    print(row["name"])
            except Exception as e:
                print(f"Error Executing Query_1: {e}")

            # Delete row based on User input
            try:
                del_row = int(input("Enter the row ID to delete: "))
                query_2 = "DELETE FROM demo WHERE id < ?"
                cursor.execute(query_2, (del_row, ))
                num_rows = cursor.rowcount
                print(f"Number of rows deleted: {num_rows}")
                db_conn.commit()
            except Exception as e:
                print(f"Error for query 2")

except sqlite3.Error as e:
    print(f"Database Connection Error: {e}")

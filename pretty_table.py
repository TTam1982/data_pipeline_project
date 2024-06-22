import sqlite3
from prettytable import PrettyTable

def fetch_data(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    conn.close()
    return columns, rows

def display_data(columns, rows):
    table = PrettyTable()
    table.field_names = columns
    for row in rows:
        table.add_row(row)
    print(table)

if __name__ == "__main__":
    db_name = "data.db"
    columns, rows = fetch_data(db_name)
    display_data(columns, rows)

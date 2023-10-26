

def create_table(db_connection):
    cursor = db_connection.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE TYPE = 'table' AND NAME = 'users_table';")
    query_result = cursor.fetchone()

    if not query_result:
        cursor.execute('''
            CREATE TABLE users_table
            (user_id INTEGER PRIMARY KEY,
            username TEXT,
            role INTEGER)
            ''')

    db_connection.commit()

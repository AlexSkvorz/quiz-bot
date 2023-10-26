

def create_table(db_connection):
    cursor = db_connection.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE TYPE = 'table' AND NAME = 'users_quiz_progress';")
    query_result = cursor.fetchone()

    if not query_result:
        cursor.execute('''
            CREATE TABLE user_quiz_progress (
            user_id INTEGER,
            quiz_id INTEGER,
            completed BOOL,
            score INTEGER,
            PRIMARY KEY (user_id, quiz_id),
            FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
            FOREIGN KEY (quiz_id) REFERENCES Questions(quiz_id) ON DELETE CASCADE)
            ''')

    db_connection.commit()
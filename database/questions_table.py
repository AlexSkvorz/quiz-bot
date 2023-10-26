

def create_table(db_connection):
    cursor = db_connection.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE TYPE = 'table' AND NAME = 'questions_table';")
    query_result = cursor.fetchone()

    if not query_result:
        cursor.execute('''
            CREATE TABLE questions (
            quiz_id INTEGER PRIMARY KEY,
            topic TEXT,
            question TEXT,
            answers TEXT,
            correct_answer TEXT)
            ''')

    db_connection.commit()
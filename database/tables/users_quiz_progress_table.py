import aiosqlite
from config.storage_config import STORAGE_CONFIG


class UserQuizProgressTable:
    @staticmethod
    async def create_table():
        async with aiosqlite.connect(STORAGE_CONFIG['DB_NAME']) as db:
            await db.execute('''
                CREATE TABLE IF NOT EXISTS user_quiz_progress_table (
                user_id INTEGER,
                quiz_id INTEGER,
                completed BOOL,
                score INTEGER,
                PRIMARY KEY (user_id, quiz_id),
                FOREIGN KEY (user_id) REFERENCES users_table(user_id) ON DELETE CASCADE,
                FOREIGN KEY (quiz_id) REFERENCES questions_table(quiz_id) ON DELETE CASCADE)
                ''')
            await db.commit()

    @staticmethod
    async def insert_user_answer(user_id, quiz_id, completed, score):
        async with aiosqlite.connect(STORAGE_CONFIG['DB_NAME']) as db:
            await db.execute("INSERT INTO user_quiz_progress_table "
                             "(user_id, quiz_id, completed, score) "
                             "VALUES(?, ?, ?, ?)",
                             parameters=(user_id, quiz_id, completed, score)
                             )
            await db.commit()

    @staticmethod
    async def fetch_user_achievements(user_id):
        async with aiosqlite.connect(STORAGE_CONFIG['DB_NAME']) as db:
            cursor = await db.execute("SELECT questions.topic, SUM(progress.score) "
                                      "FROM user_quiz_progress_table AS progress "
                                      "JOIN questions_table AS questions ON progress.quiz_id = questions.quiz_id "
                                      "WHERE progress.user_id = ? "
                                      "GROUP BY questions.topic ",
                                      parameters=(user_id,)
                                      )
            query_result = await cursor.fetchall()
            return query_result

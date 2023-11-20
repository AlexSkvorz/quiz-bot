import aiosqlite
from config.storage_config import STORAGE_CONFIG


async def create_table():
    async with aiosqlite.connect(STORAGE_CONFIG['DB_NAME']) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS questions_table (
            quiz_id INTEGER PRIMARY KEY,
            topic TEXT,
            difficult TEXT,
            question TEXT,
            answers TEXT,
            correct_answer TEXT)
            ''')
        await db.commit()


async def insert_questions(quiz_id, topic, difficult, question, answers, correct_answer):
    async with aiosqlite.connect(STORAGE_CONFIG['DB_NAME']) as db:
        await db.execute("INSERT OR IGNORE INTO questions_table"
                         " (quiz_id, topic, difficult, question, answers, correct_answer) "
                         "VALUES (?, ?, ?, ?, ?, ?)",
                         parameters=(quiz_id, topic, difficult, question, answers, correct_answer)
                         )
        await db.commit()


async def fetch_unique_topics():
    async with aiosqlite.connect(STORAGE_CONFIG['DB_NAME']) as db:
        cursor = await db.execute("SELECT DISTINCT topic FROM questions_table")
        query_result = await cursor.fetchall()
        return query_result


async def fetch_quantity_unique_questions(user_id, topic, difficult):
    async with aiosqlite.connect(STORAGE_CONFIG['DB_NAME']) as db:
        cursor = await db.execute("SELECT COUNT(questions.question) "
                                  "FROM questions_table AS questions "
                                  "LEFT JOIN user_quiz_progress_table AS progress "
                                  "ON questions.quiz_id = progress.quiz_id AND progress.user_id = ?"
                                  "WHERE progress.user_id IS NULL AND questions.topic = ? AND questions.difficult = ?",
                                  parameters=(user_id, topic, difficult,))
        query_result = await cursor.fetchone()
        return query_result


async def fetch_unique_question(user_id, topic, difficult):
    async with aiosqlite.connect(STORAGE_CONFIG['DB_NAME']) as db:
        cursor = await db.execute("SELECT questions.quiz_id, questions.question, "
                                  "questions.answers, questions.correct_answer "
                                  "FROM questions_table AS questions "
                                  "LEFT JOIN user_quiz_progress_table AS progress "
                                  "ON questions.quiz_id = progress.quiz_id AND progress.user_id = ? "
                                  "WHERE progress.user_id IS NULL AND questions.topic = ? AND questions.difficult = ? "
                                  "ORDER BY RANDOM()"
                                  "LIMIT 1 ",
                                  parameters=(user_id, topic, difficult,)
                                  )
        query_result = await cursor.fetchall()
        return query_result


async def fetch_correct_answer(quiz_id):
    async with aiosqlite.connect(STORAGE_CONFIG['DB_NAME']) as db:
        cursor = await db.execute("SELECT correct_answer FROM questions_table WHERE quiz_id = ?",
                                  parameters=(quiz_id,)
                                  )
        query_result = await cursor.fetchone()
        return query_result


async def fetch_actual_topic_and_difficult(quiz_id):
    async with aiosqlite.connect(STORAGE_CONFIG['DB_NAME']) as db:
        cursor = await db.execute("SELECT topic, difficult FROM questions_table WHERE quiz_id = ?",
                                  parameters=(quiz_id,)
                                  )
        query_result = await cursor.fetchall()
        return query_result


async def fetch_question_difficult(topic):
    async with aiosqlite.connect(STORAGE_CONFIG['DB_NAME']) as db:
        cursor = await db.execute("SELECT DISTINCT difficult FROM questions_table WHERE topic = ? ",
                                  parameters=(topic,)
                                  )
        query_result = await cursor.fetchall()
        return query_result

import aiosqlite
import json
from config.storage_config import STORAGE_CONFIG


async def create_table():
    async with aiosqlite.connect(STORAGE_CONFIG['DB_NAME']) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS questions_table (
            quiz_id INTEGER PRIMARY KEY,
            topic TEXT,
            question TEXT,
            answers TEXT,
            correct_answer TEXT)
            ''')
        await db.commit()


async def insert_questions(quiz_id, topic, question, answers, correct_answer):
    async with aiosqlite.connect(STORAGE_CONFIG['DB_NAME']) as db:
        await db.execute("INSERT OR IGNORE INTO questions_table"
                         " (quiz_id, topic, question, answers, correct_answer) VALUES (?, ?, ?, ?, ?)",
                         parameters=(quiz_id, topic, question, answers, correct_answer)
                         )
        await db.commit()

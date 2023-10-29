import aiosqlite
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


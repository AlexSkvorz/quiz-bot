import aiosqlite
from config.storage_config import STORAGE_CONFIG


async def create_table():
    async with aiosqlite.connect(STORAGE_CONFIG['DB_NAME']) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users_table
            (user_id INTEGER PRIMARY KEY,
            username TEXT,
            role INTEGER)
            ''')
        await db.commit()

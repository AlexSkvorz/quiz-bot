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


async def insert_user(user_id, username, role):
    async with aiosqlite.connect(STORAGE_CONFIG['DB_NAME']) as db:
        await db.execute('''
        INSERT OR IGNORE INTO users_table (user_id, username, role) VALUES (?, ?, ?)
        ''', parameters=(user_id, username, role)
                         )
        await db.commit()

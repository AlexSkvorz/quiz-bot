import json
import aiosqlite
from config.storage_config import STORAGE_CONFIG


async def insert_questions_data(data):
    async with aiosqlite.connect(STORAGE_CONFIG['DB_NAME']) as db:
        for item in data:
            await db.execute('''
                INSERT OR IGNORE INTO questions_table (quiz_id, topic, question, answers, correct_answer)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                item['quiz_id'], item['topic'], item['question'], json.dumps(item['answers']), item['correct_answer']))
        await db.commit()

import json
import aiosqlite


def read_data_from_json_file(file_path):
    print('11')
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


async def insert_questions_data(data, db_name):
    print('22')
    async with aiosqlite.connect(db_name) as db:
        for item in data:
            await db.execute('''
                INSERT INTO questions_table (quiz_id, topic, question, answers, correct_answer)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                item['quiz_id'], item['topic'], item['question'], json.dumps(item['answers']), item['correct_answer']))
        await db.commit()

import json
from database.questions_table import insert_questions
from config.storage_config import STORAGE_CONFIG


async def scrap_data():
    data = read_from_json_file()
    for item in data:
        await insert_questions(
            quiz_id=item["quiz_id"],
            topic=item["topic"],
            question=item["question"],
            answers=json.dumps(item["answers"]),
            correct_answer=item["correct_answer"]
        )


def read_from_json_file():
    with open(STORAGE_CONFIG['JSON_PATH'], mode='r', encoding='utf-8') as file:
        data = json.load(file)
    return data

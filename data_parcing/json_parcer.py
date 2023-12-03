import json
from config.storage_config import STORAGE_CONFIG


async def send_questions_to_database(database):
    data = read_json_file()

    try:
        for item in data:
            await database.questions_table.insert_questions(
                quiz_id=item["quiz_id"],
                topic=item["topic"],
                difficult=item["difficult"],
                question=item["question"],
                answers=json.dumps(item["answers"], ensure_ascii=False),
                correct_answer=item["correct_answer"]
            )
        return True
    except KeyError:
        return False


def read_json_file():
    with open(STORAGE_CONFIG['JSON_PATH'], mode='r', encoding='utf-8') as file:
        data = json.load(file)
    return data

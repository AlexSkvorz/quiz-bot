import json
from database.json_operations import insert_questions_data
from config.storage_config import STORAGE_CONFIG


async def scrap_data():
    data = read_data_from_json_file()
    await insert_questions_data(data)


def read_data_from_json_file():
    with open(STORAGE_CONFIG['JSON_PATH'], mode='r', encoding='utf-8') as file:
        data = json.load(file)
    return data

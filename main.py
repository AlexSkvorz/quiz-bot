import asyncio


from database.json_operations import insert_questions_data, read_data_from_json_file
from telegram_bot.quiz_bot import QuizBot
from database.create_connection import create_tables


async def main():
    await create_tables()
    quiz_bot = QuizBot().bot
    await quiz_bot.polling(none_stop=True, interval=0)
    json_file_path = 'data_questions.json' # template config
    #data = read_data_from_json_file(json_file_path)
    #await insert_questions_data(data, db_name)

if __name__ == '__main__':
    asyncio.run(main())


import asyncio

from telegram_bot.quiz_bot import QuizBot
from database.quiz_database import QuizDatabase


async def main():
    quiz_database = QuizDatabase()
    await quiz_database.create_tables()
    quiz_bot = QuizBot(database=quiz_database).bot
    await quiz_bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    asyncio.run(main())

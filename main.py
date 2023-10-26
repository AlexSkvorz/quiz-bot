import asyncio

from telegram_bot.quiz_bot import QuizBot
from database.create_connection import create_db_connection


def main():
    db_connection = create_db_connection()
    quiz_bot = QuizBot(db_connection).bot
    asyncio.run(quiz_bot.polling(none_stop=True, interval=0))


if __name__ == '__main__':
    main()

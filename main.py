import asyncio

from telegram_bot.quiz_bot import QuizBot
from database.create_connection import create_tables


async def main():
    await create_tables()
    quiz_bot = QuizBot().bot
    await quiz_bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    asyncio.run(main())


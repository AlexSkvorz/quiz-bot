import asyncio
from telegram_bot.quiz_bot import QuizBot


def main():
    quiz_bot = QuizBot().bot

    asyncio.run(quiz_bot.polling(none_stop=True, interval=0))


if __name__ == '__main__':
    print('1')
    main()

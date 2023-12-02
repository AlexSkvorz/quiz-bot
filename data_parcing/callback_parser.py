from database.questions_table import fetch_correct_answer
from telegram_bot.bot_entities.user_answer import UserAnswer
from telegram_bot.bot_entities.user_choice import UserChoice


async def parse_user_choices(user_choice):
    user_choice = user_choice.split('_difficult=')
    difficult = user_choice[1]
    user_choice = user_choice[0].split('topic=')
    topic = user_choice[1]

    return UserChoice(
        topic=topic,
        difficult=difficult
    )


async def parse_user_answer(user_answer):
    correct_answer = False

    if 'correct' in user_answer:
        user_answer = user_answer.replace('_correct', '')
        completed = 1
        score = 1
        correct_answer = True
    else:
        completed = 0
        score = 0

    user_answer = user_answer.split('quiz_id=')
    quiz_id = int(user_answer[1])

    if not correct_answer:
        correct_answer = await fetch_correct_answer(quiz_id)

    return UserAnswer(
        quiz_id=quiz_id,
        completed=completed,
        score=score,
        correct_answer=correct_answer
    )

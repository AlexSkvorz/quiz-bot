from database.users_quiz_progress_table import insert_user_answer
from database.questions_table import fetch_correct_answer, fetch_actual_topic

from telegram_bot.bot_message_generators.next_quiz_step_generator import create_next_quiz_step


async def handle_check_user_answer(bot, call):
    user_answer = call.data
    user_id = call.from_user.id
    correct_answer = None

    if 'correct' in user_answer:
        user_answer = user_answer.replace('_correct', '')
        quiz_id = int(user_answer.split('quiz_id=')[1])
        completed, score = 1, 1
    else:
        quiz_id = int(user_answer.split('quiz_id=')[1])
        completed, score = 0, 0
        correct_answer = await fetch_correct_answer(quiz_id)

    actual_topic = await fetch_actual_topic(quiz_id=quiz_id)

    await insert_user_answer(
        user_id=user_id,
        quiz_id=quiz_id,
        completed=completed,
        score=score,
    )

    await create_next_quiz_step(
        bot=bot,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        correct_answer=correct_answer,
        topic=actual_topic[0]
    )


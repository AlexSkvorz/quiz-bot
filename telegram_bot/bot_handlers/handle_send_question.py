from database.questions_table import fetch_unique_question
from telegram_bot.bot_message_generators.quiz_question_generator import send_quiz_question
import json


async def handle_send_question(bot, call):
    topic = call.data.replace('start_quiz_', '')

    unique_question = await fetch_unique_question(user_id=call.from_user.id, topic=topic)

    question = unique_question[0][0]
    answers = json.loads(unique_question[0][1])
    correct_answer = unique_question[0][2]

    await send_quiz_question(
        bot=bot,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        question=question,
        answers=answers,
        correct_answer=correct_answer
    )

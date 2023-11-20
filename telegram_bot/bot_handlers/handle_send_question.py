from database.questions_table import fetch_unique_question
from telegram_bot.bot_message_generators.quiz_question_generator import send_quiz_question
from telegram_bot.bot_message_generators.end_quiz_message_generator import send_out_questions
from data_parcing.callback_parser import parse_user_choices
import json


async def handle_send_question(bot, call):
    topic, difficult = await parse_user_choices(user_choice=call.data)

    unique_question = await fetch_unique_question(user_id=call.from_user.id, topic=topic, difficult=difficult)

    try:
        quiz_id = unique_question[0][0]
        question = unique_question[0][1]
        answers = json.loads(unique_question[0][2])
        correct_answer = unique_question[0][3]

        await send_quiz_question(
            bot=bot,
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            quiz_id=quiz_id,
            question=question,
            answers=answers,
            correct_answer=correct_answer
        )

    except IndexError:
        await send_out_questions(
            bot=bot,
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            username=call.from_user.username
        )

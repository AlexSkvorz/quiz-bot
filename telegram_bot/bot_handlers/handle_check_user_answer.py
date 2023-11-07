from database.users_quiz_progress_table import insert_user_answer
from database.questions_table import fetch_actual_topic_and_difficult
from data_parcing.callback_parser import parse_user_answer
from telegram_bot.bot_message_generators.next_quiz_step_generator import create_next_quiz_step


async def handle_check_user_answer(bot, call):
    user_id = call.from_user.id
    quiz_id, completed, score, correct_answer = await parse_user_answer(user_answer=call.data)

    query_result = await fetch_actual_topic_and_difficult(quiz_id=quiz_id)

    actual_topic = query_result[0][0]
    actual_difficult = query_result[0][1]

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
        topic=actual_topic,
        difficult=actual_difficult
    )

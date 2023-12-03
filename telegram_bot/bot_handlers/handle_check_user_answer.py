from data_parcing.callback_parser import parse_user_answer
from telegram_bot.bot_message_generators.next_quiz_step_generator import create_next_quiz_step


async def handle_check_user_answer(bot, call, database):
    user_id = call.from_user.id
    user_answer = await parse_user_answer(user_answer=call.data)

    query_result = await database.questions_table.fetch_actual_topic_and_difficult(quiz_id=quiz_id)

    actual_topic = query_result[0][0]
    actual_difficult = query_result[0][1]

    await database.user_quiz_progress_table.insert_user_answer(
        user_id=user_id,
        quiz_id=user_answer.quiz_id,
        completed=user_answer.completed,
        score=user_answer.score,
    )

    await create_next_quiz_step(
        bot=bot,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        correct_answer=user_answer.correct_answer,
        topic=actual_topic,
        difficult=actual_difficult
    )

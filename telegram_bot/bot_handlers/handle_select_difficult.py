from database.questions_table import fetch_quantity_unique_questions
from telegram_bot.bot_message_generators.start_quiz_generator import create_start_quiz_menu
from data_parcing.callback_parser import parse_user_choices


async def handle_select_difficult(bot, call):
    topic, difficult = await parse_user_choices(user_choice=call.data)

    quantity_unique_questions = await fetch_quantity_unique_questions(
        user_id=call.from_user.id,
        topic=topic,
        difficult=difficult
    )

    await create_start_quiz_menu(
        bot=bot,
        username=call.from_user.username,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        quantity_unique_questions=quantity_unique_questions[0],
        topic=topic,
        difficult=difficult
    )

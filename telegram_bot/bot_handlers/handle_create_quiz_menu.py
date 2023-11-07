from database.questions_table import fetch_unique_topics
from telegram_bot.bot_message_generators.topics_menu_generator import create_topics_menu


async def handle_create_quiz_menu(bot, chat_id, message_id):
    query_result = await fetch_unique_topics()

    unique_topics = [topic[0] for topic in query_result]

    await create_topics_menu(
        unique_topics=unique_topics,
        bot=bot,
        chat_id=chat_id,
        message_id=message_id
    )

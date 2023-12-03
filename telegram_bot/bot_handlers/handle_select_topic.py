from telegram_bot.bot_message_generators.difficult_menu_generator import create_difficult_menu


async def handle_select_topic(bot, call, database):
    topic = call.data.replace('select_topic_', '')

    query_result = await database.questions_table.fetch_question_difficult(topic=topic)

    question_difficult = [difficult[0] for difficult in query_result]

    await create_difficult_menu(
        question_difficult=question_difficult,
        bot=bot,
        message_id=call.message.message_id,
        chat_id=call.message.chat.id,
        topic=topic
    )

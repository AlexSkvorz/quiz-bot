from telegram_bot.bot_message_generators.rules_to_add_questions_generator import form_rules_to_add_questions


async def handle_add_questions(bot, call):
    await form_rules_to_add_questions(
        bot=bot,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        username=call.from_user.username
    )

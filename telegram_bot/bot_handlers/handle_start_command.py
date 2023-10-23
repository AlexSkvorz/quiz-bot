from telegram_bot.bot_message_generators.welcome_message_generator import send_welcome_message


async def handle_start_command(bot, message):
    username = message.from_user.username
    await send_welcome_message(bot=bot, chat_id=message.chat.id, username=username)

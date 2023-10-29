from telegram_bot.bot_message_generators.welcome_message_generator import send_welcome_message
from database.users_table import insert_user


async def handle_start_command(bot, message):
    user_id = message.from_user.id
    username = message.from_user.username

    await insert_user(user_id=user_id, username=username, role='user')
    await send_welcome_message(bot=bot, chat_id=message.chat.id, username=username)

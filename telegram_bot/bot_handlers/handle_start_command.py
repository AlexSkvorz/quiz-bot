from telegram_bot.bot_message_generators.welcome_message_generator import send_welcome_message


async def handle_start_command(bot, message, database):
    user_id = message.from_user.id
    username = message.from_user.username

    await database.users_table.insert_user(user_id=user_id, username=username, role='user')

    user_role = await database.users_table.fetch_user_role(user_id=user_id)

    await send_welcome_message(
        bot=bot,
        chat_id=message.chat.id,
        message_id=None,
        username=username,
        user_role=user_role[0]
    )

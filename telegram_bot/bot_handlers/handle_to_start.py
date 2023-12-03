from telegram_bot.bot_message_generators.welcome_message_generator import send_welcome_message


async def handle_to_start(bot, call, database):
    username = call.from_user.username
    user_id = call.from_user.id
    user_role = await database.users_table.fetch_user_role(user_id=user_id)

    await send_welcome_message(
        bot=bot,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        username=username,
        user_role=user_role[0]
    )

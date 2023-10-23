async def send_welcome_message(bot, chat_id, username):
    await bot.send_message(chat_id, f'Привет, {username} я асинхронный пидор!')

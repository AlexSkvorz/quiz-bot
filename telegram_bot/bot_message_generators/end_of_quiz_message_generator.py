from telegram_bot.bot_message_generators.create_inline_keyboard import create_inline_keyboard
from telegram_bot.bot_entities.bot_commands import BotCommands


async def send_out_questions(bot, chat_id, message_id, username):
    message = f'{username}, вопросы в данной теме закончились!'

    button_parameters = {'Завершить викторину': BotCommands.TO_START.value}

    markup = create_inline_keyboard(button_parameters=button_parameters)

    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=message,
        reply_markup=markup
    )

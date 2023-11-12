from telegram_bot.bot_message_generators.create_inline_keyboard import create_inline_keyboard
from telegram_bot.bot_entities.bot_commands import BotCommands


async def send_out_questions(bot, chat_id, message_id, username):
    message = f'{username}, для тебя вопросы в данной теме <b>закончились</b>, выбери другую!'

    markup = create_inline_keyboard(
        button_parameters={
            'Завершить викторину': BotCommands.TO_START.value
        }
    )

    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=message,
        parse_mode='html',
        reply_markup=markup
    )

from telegram_bot.bot_entities.bot_commands import BotCommands
from telegram_bot.bot_message_generators.create_inline_keyboard import create_inline_keyboard


async def create_difficult_menu(question_difficult, bot, chat_id, message_id, topic):
    button_parameters = {difficult: f'select_difficult_topic={topic}_difficult={difficult}'
                         for difficult in question_difficult}

    button_parameters['Вернуться назад'] = BotCommands.TO_START.value

    markup = create_inline_keyboard(button_parameters=button_parameters)

    message = 'Теперь нужно определиться, насколько <b>сложные</b> вопросы ты предпочитаешь:'

    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=message,
        parse_mode='html',
        reply_markup=markup
    )

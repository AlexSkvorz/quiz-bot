from telegram_bot.bot_entities.bot_commands import BotCommands
from telegram_bot.bot_message_generators.create_inline_keyboard import create_inline_keyboard


async def create_topics_menu(unique_topics, bot, chat_id, message_id):
    button_parameters = {topic: f'select_topic_{topic}' for topic in unique_topics}

    button_parameters['Вернуться назад'] = BotCommands.TO_START.value

    markup = create_inline_keyboard(button_parameters=button_parameters)

    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text='Какая тема тебя интересует?🧠',
        parse_mode='html',
        reply_markup=markup
    )

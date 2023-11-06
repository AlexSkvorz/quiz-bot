from telegram_bot.bot_message_generators.create_inline_keyboard import create_inline_keyboard
from constants import ADMIN
from telegram_bot.bot_entities.bot_commands import BotCommands


async def send_welcome_message(bot, chat_id, message_id, username, user_role):

    welcome_message = f'Привет, {username}, я Бот-Викторина! Выберите действие:'

    button_parameters = {
        'Викторина': BotCommands.SELECT_QUIZ.value,
        'Статистика': BotCommands.VIEW_ACHIEVEMENTS.value
    }

    if user_role == ADMIN:
        button_parameters['Добавить вопросы'] = BotCommands.ADD_QUESTIONS.value

    markup = create_inline_keyboard(
        button_parameters=button_parameters
    )

    if message_id is None:
        await bot.send_message(chat_id, welcome_message, reply_markup=markup)
    else:
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=welcome_message, reply_markup=markup)

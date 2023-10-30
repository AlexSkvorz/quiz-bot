from telegram_bot.bot_message_generators.create_buttons import create_buttons
from constants import ADMIN
from telegram_bot.bot_entities.bot_commands import BotCommands


async def send_welcome_message(bot, chat_id, username, user_role):
    welcome_message = f'Привет, {username}, я Бот-Викторина! Выберите действие:'

    button_parameters = {
        'Викторина': BotCommands.START_QUIZ.value,
        'Статистика': BotCommands.VIEW_STATISTIC.value
    }

    if user_role == ADMIN:
        button_parameters['Добавить вопросы'] = BotCommands.ADD_QUESTIONS.value

    markup = create_buttons(
        button_parameters=button_parameters
    )

    await bot.send_message(chat_id, welcome_message, reply_markup=markup)

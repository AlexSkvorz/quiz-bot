from telegram_bot.bot_message_generators.create_buttons import create_buttons
from constants import ADMIN
from telegram_bot.bot_entities.bot_commands import BotCommands


async def send_welcome_message(bot, chat_id, username, user_role):
    await bot.send_message(chat_id, f'Привет, {username}, я Бот-Викторина!')

    if user_role == ADMIN:
        button_parameters = {
            'Викторина': BotCommands.START_QUIZ.value,
            'Добавить вопросы': BotCommands.ADD_QUESTIONS.value
        }
    else:
        button_parameters = {
            'Викторина': BotCommands.START_QUIZ.value,
        }

    markup = create_buttons(
        button_parameters=button_parameters
    )

    await bot.send_message(chat_id, 'Выберите действие:', reply_markup=markup)

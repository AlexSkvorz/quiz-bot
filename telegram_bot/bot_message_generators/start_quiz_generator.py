from telegram_bot.bot_message_generators.create_inline_keyboard import create_inline_keyboard
from telegram_bot.bot_entities.bot_commands import BotCommands


async def create_start_quiz_menu(bot, username, chat_id, message_id, quantity_unique_questions, topic):
    message = f'{username}, по данной теме Вам доступно {quantity_unique_questions} вопросов!'

    button_parameters = {}

    if quantity_unique_questions > 0:
        button_parameters = {'Начать викторину': f'send_question_{topic}'}

    button_parameters['Вернуться назад'] = BotCommands.SELECT_QUIZ.value

    markup = create_inline_keyboard(button_parameters=button_parameters)

    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=message,
        reply_markup=markup
    )

from telegram_bot.bot_message_generators.create_inline_keyboard import create_inline_keyboard
from telegram_bot.bot_entities.bot_commands import BotCommands


async def create_start_quiz_menu(bot, call, quantity_unique_questions):
    message = f'{call.from_user.username}, по данной теме Вам доступно {quantity_unique_questions} вопросов!'

    button_parameters = {}

    if quantity_unique_questions > 0:
        button_parameters['Начать викторину'] = BotCommands.START_QUIZ.value

    button_parameters['Вернуться назад'] = BotCommands.TO_START.value

    markup = create_inline_keyboard(button_parameters=button_parameters)

    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=message,
        reply_markup=markup
    )

from telegram_bot.bot_entities.bot_commands import BotCommands
from telegram_bot.bot_message_generators.create_inline_keyboard import create_inline_keyboard


async def send_quiz_question(bot, chat_id, message_id, quiz_id, question, answers, correct_answer):
    message = f'{question}'

    button_parameters = {answer: f'select_answer_{answer}_quiz_id={quiz_id}' for answer in answers}

    button_parameters[correct_answer] += f'_correct'

    markup = create_inline_keyboard(button_parameters=button_parameters)

    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=message,
        reply_markup=markup
    )

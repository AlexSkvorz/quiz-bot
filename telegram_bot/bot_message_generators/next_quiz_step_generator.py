from telegram_bot.bot_message_generators.create_inline_keyboard import create_inline_keyboard


async def create_next_quiz_step(bot, chat_id, message_id, correct_answer, topic):

    if correct_answer is None:
        message = f'Вы правильно ответили на вопрос!'
    else:
        message = f'К сожалению, Вы ошиблись. Верный ответ: {correct_answer[0]}'

    button_parameters = {'Следующий вопрос': f'start_quiz_{topic}'}

    markup = create_inline_keyboard(button_parameters=button_parameters)

    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=message,
        reply_markup=markup
    )

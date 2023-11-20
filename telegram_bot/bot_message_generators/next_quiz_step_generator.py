from telegram_bot.bot_message_generators.create_inline_keyboard import create_inline_keyboard
from telegram_bot.bot_entities.bot_commands import BotCommands


async def create_next_quiz_step(bot, chat_id, message_id, correct_answer, topic, difficult):
    if type(correct_answer) is bool:
        message = f'Всё <b>верно</b>, поздравляю! Продолжай в том же духе💪'
    else:
        message = f'Упс, кажется, нужно было подумать лучше... На самом деле правильный ответ - {correct_answer[0]}🫰'

    markup = create_inline_keyboard(
        button_parameters={
            'Следующий вопрос': f'send_question_topic={topic}_difficult={difficult}',
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

from data_parcing.word_converter import get_word_form
from telegram_bot.bot_message_generators.create_inline_keyboard import create_inline_keyboard
from telegram_bot.bot_entities.bot_commands import BotCommands


async def create_start_quiz_menu(bot, username, chat_id, message_id, quantity_unique_questions, topic, difficult):
    word_form = get_word_form(quantity=quantity_unique_questions, word="вопросы")
    message = f'<b>{username}</b>, на тему {topic} ({difficult}) у меня есть {quantity_unique_questions} {word_form}'

    if quantity_unique_questions != 0:
        message += f', реши их все!🤪'
    else:
        message += f', выбери другую!🤪'

    button_parameters = {}

    if quantity_unique_questions > 0:
        button_parameters = {'Начать викторину': f'send_question_topic={topic}_difficult={difficult}'}

    button_parameters['Вернуться назад'] = BotCommands.SELECT_QUIZ.value

    markup = create_inline_keyboard(button_parameters=button_parameters)

    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=message,
        parse_mode='html',
        reply_markup=markup
    )

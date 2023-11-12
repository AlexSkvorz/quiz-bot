from data_parcing.word_converter import get_word_form
from telegram_bot.bot_message_generators.create_inline_keyboard import create_inline_keyboard
from telegram_bot.bot_entities.bot_commands import BotCommands


async def send_user_statistic_menu(bot, username, chat_id, message_id, topic_scores, total_score):
    message = f"<b>{username}</b>, а вот и твои результаты! Давай посмотрим, какие темы ты знаешь лучше:\n"
    point_word_form = get_word_form(quantity=total_score, word="балл")

    for topic, score in topic_scores.items():
        message += f"Тема: {topic} (общий балл: {score})\n"

    message += f"В сумме ты набрал {total_score} {point_word_form}, но я уверен, что ты можешь больше!❤️‍🔥"

    markup = create_inline_keyboard(
        button_parameters={
            'Вернуться в главное меню': BotCommands.TO_START.value
        }
    )

    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=message,
        parse_mode='html',
        reply_markup=markup
    )

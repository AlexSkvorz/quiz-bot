from telegram_bot.bot_message_generators.create_inline_keyboard import create_inline_keyboard
from telegram_bot.bot_entities.bot_commands import BotCommands


async def send_user_statistic_menu(bot, username, chat_id, message_id, topic_scores, total_score):
    message = f"{username}, Вот ваша статистика:\n"

    for topic, score in topic_scores.items():
        message += f"Тема: {topic}, Общий балл: {score}\n"

    message += f"Общий балл по всем темам: {total_score}"

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

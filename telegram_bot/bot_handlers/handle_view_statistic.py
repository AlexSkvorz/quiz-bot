from database.users_quiz_progress_table import fetch_user_stat_by_topic
from telegram_bot.bot_message_generators.statistic_menu_generator import send_user_statistic_menu


async def handle_view_statistic_menu(call, bot, chat_id):
    user_id = call.from_user.id
    query_user_statistic_by_topic = await fetch_user_stat_by_topic(user_id)
    message = ''
    if query_user_statistic_by_topic:
        total_score = sum(row[1] for row in query_user_statistic_by_topic)
    else:
        total_score = 0

    for row in query_user_statistic_by_topic:
        message += f'Тема: {row[0]}, Общий балл: {row[1]}\n'
    message += f'Общий балл по всем темам: {total_score}'
    print(message)
    statistic_info = message

    await send_user_statistic_menu(
        chat_id=chat_id,
        bot=bot,
        message_id=call.message.message_id,
        username=call.from_user.username,
        statistic_info=statistic_info
    )

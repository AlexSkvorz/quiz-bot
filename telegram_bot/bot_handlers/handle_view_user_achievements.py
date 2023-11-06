from database.users_quiz_progress_table import fetch_user_achievements
from telegram_bot.bot_message_generators.statistic_menu_generator import send_user_statistic_menu


async def handle_view_user_achievements(call, bot):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    query_user_statistic_by_topic = await fetch_user_achievements(user_id)
    statistic_info = ""

    if query_user_statistic_by_topic:
        total_score = sum(result[1] for result in query_user_statistic_by_topic)
        topic_scores = [f"Тема: {result[0]}, Общий балл: {result[1]}" for result in query_user_statistic_by_topic]
        statistic_info = "\n".join(topic_scores)
    else:
        total_score = 0

    statistic_info += f"\nОбщий балл по всем темам: {total_score}"

    await send_user_statistic_menu(
        chat_id=chat_id,
        bot=bot,
        message_id=call.message.message_id,
        username=call.from_user.username,
        statistic_info=statistic_info
    )

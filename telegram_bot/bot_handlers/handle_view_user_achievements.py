from database.users_quiz_progress_table import fetch_user_achievements
from telegram_bot.bot_message_generators.statistic_menu_generator import send_user_statistic_menu


async def handle_view_user_achievements(call, bot):
    user_id = call.from_user.id
    total_score = 0
    topic_scores = {}

    query_user_statistic_by_topic = await fetch_user_achievements(user_id)

    if query_user_statistic_by_topic:
        for user_stat in query_user_statistic_by_topic:
            topic = user_stat[0]
            score = user_stat[1]
            total_score += score
            topic_scores[topic] = score

    sorted_topic_scores = dict(sorted(topic_scores.items(), key=lambda user_score: user_score[1], reverse=True))

    await send_user_statistic_menu(
        chat_id=call.message.chat.id,
        bot=bot,
        message_id=call.message.message_id,
        username=call.from_user.username,
        topic_scores=sorted_topic_scores,
        total_score=total_score
    )

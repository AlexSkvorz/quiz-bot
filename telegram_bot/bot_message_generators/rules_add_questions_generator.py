from telegram_bot.bot_message_generators.create_inline_keyboard import create_inline_keyboard
from telegram_bot.bot_entities.bot_commands import BotCommands


async def form_rules_add_questions(bot, chat_id, message_id, username):
    message = f'<b>{username}</b>, чтобы добавить новые вопросы, пришли мне файл в формате <b>data_questions.json</b>'

    markup = create_inline_keyboard(
        button_parameters={
            'Вернуться назад': BotCommands.TO_START.value
        }
    )

    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=message,
        parse_mode='html',
        reply_markup=markup
    )

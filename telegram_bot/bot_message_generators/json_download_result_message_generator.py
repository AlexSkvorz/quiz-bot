from telegram_bot.bot_message_generators.create_inline_keyboard import create_inline_keyboard
from telegram_bot.bot_entities.bot_commands import BotCommands


async def form_download_result_message(bot, chat_id, download_result):
    if download_result:
        message = f'Данные были успешно добавлены'
    else:
        message = f'Не удалось добавить данные! Проверьте название файла и его сигнатуру!'

    markup = create_inline_keyboard(
        button_parameters={
            'Вернуться назад': BotCommands.TO_START.value
        }
    )

    await bot.send_message(
        chat_id=chat_id,
        text=message,
        reply_markup=markup
    )

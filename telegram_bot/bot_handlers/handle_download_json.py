from config.storage_config import STORAGE_CONFIG
from data_parcing.json_parcer import send_questions_to_database
from telegram_bot.bot_message_generators.json_download_result_message_generator import form_download_result_message


async def handle_download_json(bot, message):
    try:
        file_name = message.document.file_name.split('.')

        if file_name[1] == 'json':
            file_info = await bot.get_file(message.document.file_id)
            downloaded_file = await bot.download_file(file_info.file_path)
            src = STORAGE_CONFIG['JSON_PATH']

            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)

            download_result = await send_questions_to_database()

        else:
            download_result = False

        await form_download_result_message(
            bot=bot,
            chat_id=message.chat.id,
            download_result=download_result
        )

    except AttributeError:
        await form_download_result_message(
            bot=bot,
            chat_id=message.chat.id,
            download_result=False
        )

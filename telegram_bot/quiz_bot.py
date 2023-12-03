from telebot.async_telebot import AsyncTeleBot
from config.bot_config import BOT_CONFIG

from telegram_bot.bot_entities.bot_commands import BotCommands

from telegram_bot.bot_handlers.handle_start_command import handle_start_command
from telegram_bot.bot_handlers.handle_create_quiz_menu import handle_create_quiz_menu
from telegram_bot.bot_handlers.handle_select_topic import handle_select_topic
from telegram_bot.bot_handlers.handle_select_difficult import handle_select_difficult
from telegram_bot.bot_handlers.handle_send_question import handle_send_question
from telegram_bot.bot_handlers.handle_check_user_answer import handle_check_user_answer
from telegram_bot.bot_handlers.handle_add_questions import handle_add_questions
from telegram_bot.bot_handlers.handle_download_json import handle_download_json
from telegram_bot.bot_handlers.handle_to_start import handle_to_start
from telegram_bot.bot_handlers.handle_view_user_achievements import handle_view_user_achievements

from telegram_bot.access_decorator import admin_required


class QuizBot:
    def __init__(self, database):
        self.bot = AsyncTeleBot(BOT_CONFIG['TOKEN'])
        self.database = database

        self.initialize_handlers()

    def initialize_handlers(self):
        @self.bot.message_handler(commands=[BotCommands.START.value])
        async def start(message):
            await handle_start_command(
                bot=self.bot,
                message=message,
                database=self.database
            )

        @self.bot.callback_query_handler(func=lambda call: call.data == BotCommands.SELECT_QUIZ.value)
        async def create_quiz_menu_callback(call):
            await handle_create_quiz_menu(
                bot=self.bot,
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                database=self.database
            )

        @self.bot.callback_query_handler(func=lambda call: call.data.startswith(BotCommands.SELECT_TOPIC.value))
        async def select_topic_callback(call):
            await handle_select_topic(
                bot=self.bot,
                call=call,
                database=self.database
            )

        @self.bot.callback_query_handler(func=lambda call: call.data.startswith(BotCommands.SELECT_DIFFICULT.value))
        async def select_difficult_callback(call):
            await handle_select_difficult(
                bot=self.bot,
                call=call,
                database=self.database
            )

        @self.bot.callback_query_handler(func=lambda call: call.data.startswith(BotCommands.SEND_QUESTION.value))
        async def send_question_callback(call):
            await handle_send_question(
                bot=self.bot,
                call=call,
                database=self.database
            )

        @self.bot.callback_query_handler(func=lambda call: call.data.startswith(BotCommands.SELECT_ANSWER.value))
        async def check_user_answer_callback(call):
            await handle_check_user_answer(
                bot=self.bot,
                call=call,
                database=self.database
            )

        @self.bot.callback_query_handler(func=lambda call: call.data == BotCommands.ADD_QUESTIONS.value)
        async def add_questions_callback(call):
            await handle_add_questions(bot=self.bot, call=call)
            self.bot.register_message_handler(download_json_callback)

        @self.bot.message_handler(content_types=['document'])
        @admin_required
        async def download_json_callback(message):
            await handle_download_json(
                bot=self.bot,
                message=message,
                database=self.database
            )

        @self.bot.callback_query_handler(func=lambda call: call.data == BotCommands.TO_START.value)
        async def to_start_callback(call):
            await handle_to_start(
                bot=self.bot,
                call=call,
                database=self.database
            )

        @self.bot.callback_query_handler(func=lambda call: call.data == BotCommands.VIEW_ACHIEVEMENTS.value)
        async def view_user_achievements_callback(call):
            await handle_view_user_achievements(
                bot=self.bot,
                call=call,
                database=self.database
            )

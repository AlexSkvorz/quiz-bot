from telebot.async_telebot import AsyncTeleBot
from config.bot_config import BOT_CONFIG

from telegram_bot.bot_entities.bot_commands import BotCommands

from telegram_bot.bot_handlers.handle_start_command import handle_start_command
from telegram_bot.bot_handlers.handle_create_quiz_menu import handle_create_quiz_menu
from telegram_bot.bot_handlers.handle_select_topic import handle_select_topic
from telegram_bot.bot_handlers.handle_send_question import handle_send_question
from telegram_bot.bot_handlers.handle_check_user_answer import handle_check_user_answer


class QuizBot:
    def __init__(self):
        self.bot = AsyncTeleBot(BOT_CONFIG['TOKEN'])

        self.initialize_handlers()

    def initialize_handlers(self):
        @self.bot.message_handler(commands=[BotCommands.START.value])
        async def start(message):
            await handle_start_command(bot=self.bot, message=message)

        @self.bot.callback_query_handler(func=lambda call: call.data == BotCommands.SELECT_QUIZ.value)
        async def create_quiz_menu_callback(call):
            await handle_create_quiz_menu(
                bot=self.bot,
                chat_id=call.message.chat.id,
                message_id=call.message.message_id
            )

        @self.bot.callback_query_handler(func=lambda call: call.data.startswith(BotCommands.SELECT_TOPIC.value))
        async def select_topic_callback(call):
            await handle_select_topic(
                bot=self.bot,
                call=call
            )

        @self.bot.callback_query_handler(func=lambda call: call.data.startswith(BotCommands.START_QUIZ.value))
        async def send_question_callback(call):
            await handle_send_question(
                bot=self.bot,
                call=call
            )

        @self.bot.callback_query_handler(func=lambda call: call.data.startswith(BotCommands.SELECT_ANSWER.value))
        async def check_user_answer_callback(call):
            await handle_check_user_answer(
                bot=self.bot,
                call=call
            )

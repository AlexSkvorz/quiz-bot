from telebot.async_telebot import AsyncTeleBot
from config.bot_config import BOT_CONFIG
from telegram_bot.bot_entities.bot_commands import BotCommands
from telegram_bot.bot_handlers.handle_start_command import handle_start_command


class QuizBot:
    def __init__(self):
        self.bot = AsyncTeleBot(BOT_CONFIG['TOKEN'])

        self.initialize_handlers()

    def initialize_handlers(self):
        @self.bot.message_handler(commands=[BotCommands.START.value])
        async def start(message):
            await handle_start_command(bot=self.bot, message=message)

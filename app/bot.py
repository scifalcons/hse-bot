import logging

from telebot import TeleBot
from telebot.types import Message

log = logging.getLogger(__name__)


def init(bot: TeleBot) -> None:
    @bot.message_handler(commands=["start", "help"])
    def send_welcome(message: Message) -> None:
        """Handle /start and /help commands."""
        bot.reply_to(
            message,
            "Send me a YouTube or Instagram link, and I'll download the media for you!",
        )

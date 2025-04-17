import logging
import os

from telebot import TeleBot

from app import bot

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
log = logging.getLogger(__name__)


def main() -> None:
    log.info("Starting telegram bot...")
    bot = TeleBot(os.environ["BOT_TOKEN"])
    bot.init(bot)
    bot.infinity_polling()


if __name__ == "__main__":
    main()

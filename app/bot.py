import logging

from telebot import TeleBot
from telebot.types import Message

log = logging.getLogger(__name__)

SPECIAL_MENTION = "@all"


def init(bot: TeleBot) -> None:
    @bot.message_handler(commands=["start"])
    def main(message: Message) -> None:
        bot.send_message(message.chat.id, "hello")

    # TODO: decompose filter into own function
    @bot.message_handler(
        func=lambda message: message.chat.type in ["group", "supergroup"]
        and SPECIAL_MENTION in message.text.lower()
    )
    def mention_all_admins(message: Message) -> None:
        chat_id = message.chat.id

        admins = bot.get_chat_administrators(chat_id)

        mentions = []
        for admin in admins:
            user = admin.user
            mention = f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"
            mentions.append(mention)

        if mentions:
            reply_text = "Внимание: " + ", ".join(mentions)
        else:
            reply_text = "Не удалось получить список администраторов."

        bot.send_message(chat_id, reply_text, parse_mode="HTML")

import telebot  # type: ignore

bot = telebot.TeleBot("")


bot.polling(none_stop=True)

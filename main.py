import telebot


bot = telebot.TeleBot("6701680611:AAEtvp-iwsfhN4yWPzbSV78pHxUveaOA3Vc")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет!")


bot.polling()
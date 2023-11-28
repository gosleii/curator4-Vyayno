import telebot

bot = telebot.TeleBot('1125811332:AAGMQFHCEHV1Lswxr7aodPbgpyhVkQXVP6k')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Сообщение')


@bot.message_handler(commands=['run'])
def main(message):
    bot.send_message(message.chat.id, '*Бежим!* \n Бежииим создавать бота!', parse_mode='Markdown')


@bot.message_handler(commands=['pashalka'])
def main(message):
    bot.send_message(message.chat.id, "[ссылка](https://youtu.be/dQw4w9WgXcQ?si=6vUBgU_roQX9IpGK)", parse_mode='Markdown')


bot.infinity_polling()
import telebot

bot = telebot.TeleBot('6174644288:AAHRP-Rh9YqSWpQn4qnGFMWnpiyTaMhaJqs')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_mesage(message.chat.id, 'Сообщение')


@bot.message_handler(commands=['run'])
def main(message):
    bot.send_mesage(message.chat.id, '*Бежим!* \n Бежииим создавать бота!', parse_mode='Markdown')


@bot.message_handler(commands=['pashalka'])
def main(message):
    bot.send_mesage(message.chat.id, '[ссылка] (https://youtu.be/dQw4w9WgXcQ?si=6vUBgU_roQX9IpGK)',
                    parse_mode='Markdown')


bot.infinity_polling()
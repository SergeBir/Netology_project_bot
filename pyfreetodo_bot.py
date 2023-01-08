import telebot

token = '5876915604:AAHhU-c5h21MiAkNPVWMQSqP1nb-IS3v-4U'

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)

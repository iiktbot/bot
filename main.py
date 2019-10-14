import telebot
import os
from flask import Flask, request


bot = telebot.TeleBot("593642481:AAEuoLHI.....")

server = Flask(__name__)


@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
    user_markup.row('/start','/info')
    start_text = str('Привет, '+message.from_user.first_name+'!\nЯ бот на Heroku.')
    bot.send_message(chat_id=1154965888, text=start_text, parse_mode='Markdown')


@server.route('/' + tokenBot.TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://test-new-new.herokuapp.com/' + tokenBot.TOKEN)
    return "!", 200


if __name__ == '__main__':
    server.debug = True
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

import logging
import telegram
import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Updater, CommandHandler

TOKEN = os.environ['TOKEN']
HOST = os.environ['HOST']
PORT = os.environ['PORT']
URL = os.environ['URL']

bot = telegram.Bot(TOKEN)
app = Flask(__name__)
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

logging.basicConfig(
    level=logging.DEBUG, format='%(levelname)s: %(name)s - %(message)s')
logger = logging.getLogger(__name__)


def start_cmd(update, context):
    user = update.effective_user
    user_id = user['id']
    context.bot.send_message(user_id, 'started')


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return '!'


@app.route('/' + TOKEN, methods=['GET', 'POST'])
def process_webhook():
    if request.method == 'POST':
        update = telegram.update.Update.de_json(request.get_json(force=True), bot)
        dp.process_update(update)
    return '!'


def main():
    start_cmd_handler = CommandHandler('start', start_cmd)
    dp.add_handler(start_cmd_handler)
    bot.setWebhook(webhook_url='https://%s:%s/%s' % (HOST, PORT, TOKEN))

if __name__ == "__main__":
    main()
    app.run(host=HOST, port=PORT, debug=True)

import telebot # подключение библиотеки pyTelegramBotAPI

import logging # библиотека журнала


# для запуска скриптов

from subprocess import call

# настройки для журнала

logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('logs.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

# создание бота с его токеном API

bot = telebot.TeleBot('642122532:AAGKg4s2_ffJqDNTrqvbI7-qeFRxNEOBPV8')

# текст справки

help_string = []
help_string.append("Это простой *тестовый бот*, созданный в обучающих целях.\n\n")
help_string.append("/start - выводит приветствие;\n")
help_string.append("/help - отображает эту справку;\n")
help_string.append("/server - присылает статус сервера.")

# --- команды


@bot.message_handler(commands=['start'])
def send_start(message):
    # отправка простого сообщения

    bot.send_message(message.chat.id, "Привет, я тестовый бот! Отправьте мне /help для вывод справки.")

@bot.message_handler(commands=['help'])
def send_help(message):
    # отправка сообщения с поддержкой разметки Markdown

    bot.send_message(message.chat.id, "".join(help_string), parse_mode="Markdown")

bot.polling()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask, apiai, json, telebot, os, requests, urllib, time, random, messages, stickers, schedule, students
from flask import Flask, request
from telebot import types
from datetime import date, timedelta
from random import randrange

TOKEN = os.environ["TOKEN"]
bot = telebot.TeleBot(TOKEN, threaded=False)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_message(message):
    cid = message.chat.id
    bot.send_message(cid, "привет, чем могу быть полезен?")

"""
def ai_message(bot, update):
    if "бот" in msg and not any(words in msg for words in messages_tuple):
        bot.send_message(cid, dialogflow_response)
    else:
        bot.send_message(cid, unexpected_phrase)
"""

@app.route('/' + TOKEN, methods=['POST'])
def get_messages():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "", 200

@app.route('/')
def process_webhook():
    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(url="https://iiktbot.herokuapp.com/" + TOKEN)
    return "", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 443)))

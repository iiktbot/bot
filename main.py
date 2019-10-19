#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask, apiai, json, telebot, os, requests, urllib, time, random
from flask import Flask, request
from telebot import types
from datetime import date, timedelta
from random import randrange

token = '924107471:AAE3pzrmRZbXTWShfsBw8gwOadxvYUhDDNo'
bot = telebot.TeleBot(token, threaded=False)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "привет, чем могу быть полезен?")

@bot.message_handler(content_types=['text'])
def predefined_messages(message):
    msg = message.text.lower()
    mid = message.message_id
    cid = message.chat.id
    uid = message.from_user.id

    first_group = {
        ('Виталий'): 405299021,
        ('Юля'): 393708492,
        ('Андрей'): 416924459,
        ('Влад'): 613759219,
        ('Женя'): 548116631,
        ('Карина'): 379537100,
        ('Денис'): 635991556,
        ('Дима'): 349737926,
        ('Дима'): 451287655,
        ('Степан'): 469338261,
        ('Денис'): 542413243,
        ('Женя'): 692445612,
        ('Полина'): 429045248,
        ('Саша'): 52960692
    }
    second_group = {
        ('Илья'): 358734682,
        ('Саша'): 537784508,
        ('Богдан'): 448401733,
        ('Влад'): 643705130,
        ('Леша'): 605903256,
        ('Олег'): 384343953,
        ('Влад'): 655298761,
        ('Дима'): 384173347,
        ('Денис'): 780853105
    }
    first_group_eng = {
        ('Виталий'): 405299021,
        ('Влад'): 643705130,
        ('Андрей'): 416924459,
        ('Денис'): 542413243,
        ('Денис'): 635991556,
        ('Дима'): 349737926,
        ('Дима'): 451287655,
        ('Женя'): 692445612,
        ('Полина'): 123456789,
        ('Саша'): 52960692,
        ('Денис'): 780853105,
        ('Дима'): 384173347,
        ('Влад'): 655298761
    }
    second_group_eng = {
        ('Юля'): 393708492,
        ('Карина'): 379537100,
        ('Женя'): 548116631,
        ('Влад'): 613759219,
        ('Степан'): 469338261,
        ('Олег'): 384343953,
        ('Илья'): 358734682,
        ('Саша'): 537784508,
        ('Богдан'): 448401733,
        ('Леша'): 605903256
    }
    if "0 or 1?" in msg:
        if uid in first_group.values():
            bot.send_message(cid, "1")
        else:
            bot.send_message(cid, "0")


@app.route('/' + token, methods=['POST'])
def get_messages():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "", 200

@app.route('/')
def process_webhook():
    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(url="https://iiktbot.herokuapp.com/" + token)
    return "", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 443)))

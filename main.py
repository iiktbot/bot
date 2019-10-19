#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask, apiai, json, telebot, os, requests, urllib, time, random
from flask import Flask, request
from telebot import types
from datetime import date, timedelta
from random import randrange

token = '642122532:AAGKg4s2_ffJqDNTrqvbI7-qeFRxNEOBPV8'
secret = '05f6b51a6e22d6e7d47f1235f26590b5dee83ece1b8da0719569a4b5a09b1ea2'
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
    all_students = {
        ** first_group,
        ** second_group
    }

    SCHEDULE_MONDAY_DAYOFF = "\n\nПАР НЕТ"
    SCHEDULE_TUESDAY_DAYOFF = "\n\nПАР НЕТ"
    SCHEDULE_WEDNESDAY_DAYOFF = "\n\nПАР НЕТ"
    SCHEDULE_THURSDAY_DAYOFF = "\n\nПАР НЕТ"
    SCHEDULE_FRIDAY_DAYOFF = "\n\nПАР НЕТ"
    SCHEDULE_SATURDAY_DAYOFF = "\n\nПАР НЕТ"
    SCHEDULE_SUNDAY_DAYOFF = "\n\nПАР НЕТ"

    CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_FULLWEEK = "\n\nпонедельник\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n11:40-13:00 — ООП\n13:05-14:25 — ООП\n\nпятница\n08:30-09:50 — КОМП. СХЕМ.\n10:00-11:20 — КОМП. СХЕМ."
    CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_FULLWEEK = "\n\nпонедельник\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n11:40-13:00 — ООП\n13:05-14:25 — ООП\n\nпятница\n10:00-11:20 — КОМП. СХЕМ.\n13:05-14:25 — КОМП. СХЕМ."
    CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_FULLWEEK = "\n\nпонедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n13:05-14:25 — ООП\n\nпятница\n13:05-14:25 — ООП\n14:30-15:50 — ООП"
    CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_FULLWEEK = "\n\nпонедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n13:05-14:25 — ООП\n\nпятница\n13:05-14:25 — ООП\n14:30-15:50 — ООП"
    CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_FULLWEEK = "\n\nпонедельник\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n11:40-13:00 — ООП\n13:05-14:25 — ООП\n\nпятница\nПАР НЕТ"
    CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_FULLWEEK = "\n\nпонедельник\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n11:40-13:00 — ООП\n13:05-14:25 — ООП\n\nпятница\nПАР НЕТ"
    CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_FULLWEEK = "\n\nпонедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n13:05-14:25 — ООП\n\nпятница\n13:05-14:25 — ООП\n14:30-15:50 — ООП"
    CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_FULLWEEK = "\n\nпонедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n13:05-14:25 — ООП\n\nпятница\n13:05-14:25 — ООП\n14:30-15:50 — ООП"

    CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY = "\n\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ."
    CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY = "\n\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ."
    CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY = "\n\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ."
    CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY = "\n\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ."
    CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY = "\n\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ."
    CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY = "\n\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ."
    CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY = "\n\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ."
    CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY = "\n\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ."

    CS18_SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY = SCHEDULE_TUESDAY_DAYOFF
    CS18_SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY = SCHEDULE_TUESDAY_DAYOFF
    CS18_SCHEDULE_DARKWEEK_1GROUP_TUESDAY = SCHEDULE_TUESDAY_DAYOFF
    CS18_SCHEDULE_DARKWEEK_2GROUP_TUESDAY = SCHEDULE_TUESDAY_DAYOFF

    CS18_SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY = "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР."
    CS18_SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY = "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР."
    CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY = "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР."
    CS18_SCHEDULE_DARKWEEK_2GROUP_WEDNESDAY = "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР."

    CS18_SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY = "\n\n11:40-13:00 — ООП\n13:05-14:25 — ООП"
    CS18_SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY = "\n\n13:05-14:25 — ООП"
    CS18_SCHEDULE_DARKWEEK_1GROUP_THURSDAY = "\n\n11:40-13:00 — ООП\n13:05-14:25 — ООП"
    CS18_SCHEDULE_DARKWEEK_2GROUP_THURSDAY = "\n\n13:05-14:25 — ООП"

    CS18_SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY = "\n\n08:30-09:50 — КОМП. СХЕМ.\n10:00-11:20 — КОМП. СХЕМ."
    CS18_SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY = "\n\n10:00-11:20 — КОМП. СХЕМ.\n13:05-14:25 — КОМП. СХЕМ."
    CS18_SCHEDULE_DARKWEEK_1GROUP_FRIDAY = SCHEDULE_FRIDAY_DAYOFF
    CS18_SCHEDULE_DARKWEEK_2GROUP_FRIDAY = "\n\n13:05-14:25 — ООП\n14:30-15:50 — ООП"

    CS18_SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY = SCHEDULE_SATURDAY_DAYOFF
    CS18_SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY = SCHEDULE_SATURDAY_DAYOFF
    CS18_SCHEDULE_DARKWEEK_1GROUP_SATURDAY = SCHEDULE_SATURDAY_DAYOFF
    CS18_SCHEDULE_DARKWEEK_2GROUP_SATURDAY = SCHEDULE_SATURDAY_DAYOFF

    CS18_SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY = SCHEDULE_SUNDAY_DAYOFF
    CS18_SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY = SCHEDULE_SUNDAY_DAYOFF
    CS18_SCHEDULE_DARKWEEK_1GROUP_SUNDAY = SCHEDULE_SUNDAY_DAYOFF
    CS18_SCHEDULE_DARKWEEK_2GROUP_SUNDAY = SCHEDULE_SUNDAY_DAYOFF

    if (date.today().isocalendar()[1] % 2) == 0:
        weekorder = True
        week = "светлая"
    else:
        weekorder = False
        week = "тёмная"
    if date.today().weekday() == 0:
        today = "понедельник"
        tomorrow = "вторник"
        yesterday = "воскресенье"
    elif date.today().weekday() == 1:
        today = "вторник"
        tomorrow = "среда"
        yesterday = "понедельник"
    elif date.today().weekday() == 2:
        today = "среда"
        tomorrow = "четверг"
        yesterday = "вторник"
    elif date.today().weekday() == 3:
        today = "четверг"
        tomorrow = "пятница"
        yesterday = "среда"
    elif date.today().weekday() == 4:
        today = "пятница"
        tomorrow = "суббота"
        yesterday = "четверг"
    elif date.today().weekday() == 5:
        today = "суббота"
        tomorrow = "воскресенье"
        yesterday = "пятница"
    elif date.today().weekday() == 6:
        today = "воскресенье"
        tomorrow = "понедельник"
        yesterday = "суббота"

    student_name = ""
    student_group = ""

    for name, identifier in first_group.items():
        if uid == identifier:
            student_group = "первая группа"
    for name, identifier in second_group.items():
        if uid == identifier:
            student_group = "вторая группа"
    for name, identifier in all_students.items():
        if uid == identifier:
            student_name = list(all_students.keys())[list(all_students.values()).index(identifier)].lower() + ", "
            
    week_template = " группа / " + week + " неделя"
    today_template = student_name + student_group + " (" + today + ")"
    yesterday_template = student_name + student_group + " (" + yesterday + ")"
    tomorrow_template = student_name + student_group + " (" + tomorrow + ")"

    classes_tuple = "пары", "парам", "расписание", "расписанию", "предметы", "предметам"
    day_tuple = "какой день", "какой сейчас день", "какой сегодня день"
    week_tuple = "какая неделя", "какая сейчас неделя", "какая сегодня неделя"
    days_tuple = "сегодня", "вчера", "завтра"
    today_tuple = "вчера", "завтра"
    yesterday_tuple = "сегодня", "завтра"
    tomorrow_tuple = "вчера", "сегодня"
    weekdays_tuple = "понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье", "среду", "пятницу", "субботу", "пн", "вт", "ср", "чт", "пт", "сб", "вс"
    monday_tuple = "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье", "среду", "пятницу", "субботу", "вт", "ср", "чт", "пт", "сб", "вс"
    tuesday_tuple = "понедельник", "среда", "четверг", "пятница", "суббота", "воскресенье", "среду", "пятницу", "субботу", "пн", "ср", "чт", "пт", "сб", "вс"
    wednesday_tuple = "понедельник", "вторник", "четверг", "пятница", "суббота", "воскресенье", "пятницу", "субботу", "пн", "вт", "чт", "пт", "сб", "вс"
    thursday_tuple = "понедельник", "вторник", "среда", "пятница", "суббота", "воскресенье", "среду", "пятницу", "субботу", "пн", "вт", "ср", "пт", "сб", "вс"
    friday_tuple = "понедельник", "вторник", "среда", "четверг", "суббота", "воскресенье", "среду", "субботу", "пн", "вт", "ср", "чт", "сб", "вс"
    saturday_tuple = "понедельник", "вторник", "среда", "четверг", "пятница", "воскресенье", "среду", "пятницу", "пн", "вт", "ср", "чт", "пт", "вс"
    sunday_tuple = "понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "среду", "пятницу", "субботу", "пн", "вт", "ср", "чт", "пт", "сб"
    exceptions_tuple = "поза", "после"
    messages_tuple = "пары", "парам", "расписание", "расписанию", "предметы", "предметам", "какой день", "какой сейчас день", "какой сегодня день", "какая неделя", "какая сейчас неделя", "какая сегодня неделя", "сегодня", "вчера", "завтра", "понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье", "среду", "пятницу", "субботу", "пн", "вт", "ср", "чт", "пт", "сб", "вс"

    meme_url = str("https://t.me/LaQeque/" + str(random.randint(5, 39946)))
    meme_req = requests.get(meme_url)

    if "мем" in msg or "meme" in msg:
        if uid in all_students.values():
            bot.send_chat_action(cid, "upload_photo")
            bot.send_photo(cid, meme_url)
        else:
            bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)

    if any(words in msg for words in week_tuple):
        bot.send_message(cid, "сейчас " + week + " неделя", reply_to_message_id=mid)

    if weekorder == True:
        if date.today().weekday() == 0 and any(words in msg for words in day_tuple):
            bot.send_message(cid, "сегодня светлый " + today, reply_to_message_id=mid)
        elif date.today().weekday() == 1 and any(words in msg for words in day_tuple):
            bot.send_message(cid, "сегодня светлый " + today, reply_to_message_id=mid)
        elif date.today().weekday() == 2 and any(words in msg for words in day_tuple):
            bot.send_message(cid, "сегодня светлая " + today, reply_to_message_id=mid)
        elif date.today().weekday() == 3 and any(words in msg for words in day_tuple):
            bot.send_message(cid, "сегодня светлый " + today, reply_to_message_id=mid)
        elif date.today().weekday() == 4 and any(words in msg for words in day_tuple):
            bot.send_message(cid, "сегодня светлая " + today, reply_to_message_id=mid)
        elif date.today().weekday() == 5 and any(words in msg for words in day_tuple):
            bot.send_message(cid, "сегодня светлая " + today, reply_to_message_id=mid)
        elif date.today().weekday() == 6 and any(words in msg for words in day_tuple):
            bot.send_message(cid, "сегодня светлое " + today, reply_to_message_id=mid)
        if any(words in msg for words in classes_tuple):
            if not any(words in msg for words in days_tuple) and not any(words in msg for words in weekdays_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.values():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 1:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 2:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 3:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 4:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 5:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 6:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.values():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 1:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 2:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 3:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 4:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 5:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 6:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
            elif "сегодня" in msg and not any(words in msg for words in today_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.values():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 1:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 2:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 3:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 4:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 5:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 6:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.values():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 1:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 2:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 3:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 4:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 5:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 6:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
            elif "вчера" in msg and not any(words in msg for words in yesterday_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.values():
                    if date.today().weekday() - 1 == 0:
                        if uid in first_group_eng.values():
                            bot.send_message(cid, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 1:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 2:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 3:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 4:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 5:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 6:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.values():
                    if date.today().weekday() - 1 == 0:
                        if uid in first_group_eng.values():
                            bot.send_message(cid, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 1:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 2:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 3:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 4:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 5:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 6:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
            elif "завтра" in msg and not any(words in msg for words in tomorrow_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.values():
                    if date.today().weekday() + 1 == 7:
                        if uid in first_group_eng.values():
                            bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 1:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 2:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 3:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 4:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 5:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 6:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.values():
                    if date.today().weekday() + 1 == 7:
                        if uid in first_group_eng.values():
                            bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 1:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 2:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 3:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 4:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 5:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 6:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
            elif not any(words in msg for words in days_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.values():
                    if "понедельник" in msg or "пн" in msg and not any(words in msg for words in monday_tuple):
                        if uid in first_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif "вторник" in msg or "вт" in msg and not any(words in msg for words in tuesday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif "среда" in msg or "среду" in msg or "ср" in msg and not any(words in msg for words in wednesday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif "четверг" in msg or "чт" in msg and not any(words in msg for words in thursday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif "пятница" in msg or "пятницу" in msg or "пт" in msg and not any(words in msg for words in friday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif "суббота" in msg or "субботу" in msg or "сб" in msg and not any(words in msg for words in saturday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif "воскресенье" in msg or "вс" in msg and not any(words in msg for words in sunday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.values():
                    if "понедельник" in msg or "пн" in msg and not any(words in msg for words in monday_tuple):
                        if uid in first_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif "вторник" in msg or "вт" in msg and not any(words in msg for words in tuesday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif "среда" in msg or "среду" in msg or "ср" in msg and not any(words in msg for words in wednesday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif "четверг" in msg or "чт" in msg and not any(words in msg for words in thursday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif "пятница" in msg or "пятницу" in msg or "пт" in msg and not any(words in msg for words in friday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif "суббота" in msg or "субботу" in msg or "сб" in msg and not any(words in msg for words in saturday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif "воскресенье" in msg or "вс" in msg and not any(words in msg for words in sunday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
        if "schedule" in msg:
            if uid in first_group.values():
                if uid in first_group_eng.values():
                    bot.send_message(cid, student_group + week_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_FULLWEEK)
                elif uid in second_group_eng.values():
                    bot.send_message(cid, student_group + week_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_FULLWEEK)
            elif uid in second_group.values():
                if uid in first_group_eng.values():
                    bot.send_message(cid, student_group + week_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_FULLWEEK)
                elif uid in second_group_eng.values():
                    bot.send_message(cid, student_group + week_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_FULLWEEK)
            else:
                bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
    elif weekorder == False:
        if date.today().weekday() == 0 and any(words in msg for words in day_tuple):
            bot.send_message(cid, "сегодня тёмный " + today, reply_to_message_id=mid)
        elif date.today().weekday() == 1 and any(words in msg for words in day_tuple):
            bot.send_message(cid, "сегодня тёмный " + today, reply_to_message_id=mid)
        elif date.today().weekday() == 2 and any(words in msg for words in day_tuple):
            bot.send_message(cid, "сегодня тёмная " + today, reply_to_message_id=mid)
        elif date.today().weekday() == 3 and any(words in msg for words in day_tuple):
            bot.send_message(cid, "сегодня тёмный " + today, reply_to_message_id=mid)
        elif date.today().weekday() == 4 and any(words in msg for words in day_tuple):
            bot.send_message(cid, "сегодня тёмная " + today, reply_to_message_id=mid)
        elif date.today().weekday() == 5 and any(words in msg for words in day_tuple):
            bot.send_message(cid, "сегодня тёмная " + today, reply_to_message_id=mid)
        elif date.today().weekday() == 6 and any(words in msg for words in day_tuple):
            bot.send_message(cid, "сегодня тёмное " + today, reply_to_message_id=mid)
        if any(words in msg for words in classes_tuple):
            if not any(words in msg for words in days_tuple) and not any(words in msg for words in weekdays_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.values():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 1:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 2:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 3:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 4:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 5:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 6:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.values():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 1:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 2:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 3:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 4:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 5:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 6:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
            elif "сегодня" in msg and not any(words in msg for words in today_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.values():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 1:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 2:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 3:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 4:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 5:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 6:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.values():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 1:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 2:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 3:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 4:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 5:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 6:
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
            elif "вчера" in msg and not any(words in msg for words in yesterday_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.values():
                    if date.today().weekday() - 1 == 0:
                        if uid in first_group_eng.values():
                            bot.send_message(cid, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 1:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 2:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 3:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 4:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 5:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 6:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.values():
                    if date.today().weekday() - 1 == 0:
                        if uid in first_group_eng.values():
                            bot.send_message(cid, yesterday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, yesterday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 1:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 2:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 3:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 4:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 5:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 6:
                        bot.send_message(cid, yesterday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
            elif "завтра" in msg and not any(words in msg for words in tomorrow_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.values():
                    if date.today().weekday() + 1 == 7:
                        if uid in first_group_eng.values():
                            bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 1:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 2:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 3:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 4:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 5:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_DARKWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 6:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_DARKWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.values():
                    if date.today().weekday() + 1 == 7:
                        if uid in first_group_eng.values():
                            bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 1:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 2:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_DARKWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 3:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 4:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 5:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_DARKWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 6:
                        bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_DARKWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
            elif not any(words in msg for words in days_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.values():
                    if "понедельник" in msg or "пн" in msg and not any(words in msg for words in monday_tuple):
                        if uid in first_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif "вторник" in msg or "вт" in msg and not any(words in msg for words in tuesday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif "среда" in msg or "среду" in msg or "ср" in msg and not any(words in msg for words in wednesday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif "четверг" in msg or "чт" in msg and not any(words in msg for words in thursday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif "пятница" in msg or "пятницу" in msg or "пт" in msg and not any(words in msg for words in friday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif "суббота" in msg or "субботу" in msg or "сб" in msg and not any(words in msg for words in saturday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif "воскресенье" in msg or "вс" in msg and not any(words in msg for words in sunday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.values():
                    if "понедельник" in msg or "пн" in msg and not any(words in msg for words in monday_tuple):
                        if uid in first_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.values():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif "вторник" in msg or "вт" in msg and not any(words in msg for words in tuesday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif "среда" in msg or "среду" in msg or "ср" in msg and not any(words in msg for words in wednesday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif "четверг" in msg or "чт" in msg and not any(words in msg for words in thursday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif "пятница" in msg or "пятницу" in msg or "пт" in msg and not any(words in msg for words in friday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif "суббота" in msg or "субботу" in msg or "сб" in msg and not any(words in msg for words in saturday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif "воскресенье" in msg or "вс" in msg and not any(words in msg for words in sunday_tuple):
                        bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
        if "schedule" in msg:
            if uid in first_group.values():
                if uid in first_group_eng.values():
                    bot.send_message(cid, student_group + week_template + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_FULLWEEK)
                elif uid in second_group_eng.values():
                    bot.send_message(cid, student_group + week_template + CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_FULLWEEK)
            elif uid in second_group.values():
                if uid in first_group_eng.values():
                    bot.send_message(cid, student_group + week_template + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_FULLWEEK)
                elif uid in second_group_eng.values():
                    bot.send_message(cid, student_group + week_template + CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_FULLWEEK)
            else:
                bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
"""
def ai_message(bot, update):
    if "бот" in msg and not any(words in msg for words in messages_tuple):
        bot.send_message(cid, dialogflow_response)
    else:
        bot.send_message(cid, unexpected_phrase)
"""
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
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

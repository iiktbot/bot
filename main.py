#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask, apiai, json, telebot, os, requests, urllib, time, random
from flask import Flask, request
from telebot import types
from datetime import date, timedelta
from random import randrange

TOKEN = os.environ["TOKEN"]
bot = telebot.TeleBot(TOKEN, skip_pending=True, threaded=False)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_message(message):
    cid = message.chat.id
    bot.send_message(cid, "привет, чем могу быть полезен?")

@bot.message_handler(content_types=['text'])
def predefined_messages(message):
    msg = message.text.lower()
    mid = message.message_id
    cid = message.chat.id
    uid = message.from_user.id

    first_group = {
        405299021: 'Виталий',
        393708492: 'Юля',
        416924459: 'Андрей',
        613759219: 'Влад',
        548116631: 'Женя',
        379537100: 'Карина',
        635991556: 'Денис',
        349737926: 'Дима',
        451287655: 'Дима',
        469338261: 'Степан',
        542413243: 'Денис',
        692445612: 'Женя',
        429045248: 'Полина',
        52960692: 'Саша'
    }
    second_group = {
        358734682: 'Илья',
        537784508: 'Саша',
        448401733: 'Богдан',
        643705130: 'Влад',
        605903256: 'Леша',
        384343953: 'Олег',
        655298761: 'Влад',
        384173347: 'Дима',
        780853105: 'Денис'
    }
    first_group_eng = {
        405299021: 'Виталий',
        643705130: 'Влад',
        416924459: 'Андрей',
        542413243: 'Денис',
        635991556: 'Денис',
        349737926: 'Дима',
        451287655: 'Дима',
        692445612: 'Женя',
        123456789: 'Полина',
        52960692: 'Саша',
        780853105: 'Денис',
        384173347: 'Дима',
        655298761: 'Влад'
    }
    second_group_eng = {
        393708492: 'Юля',
        379537100: 'Карина',
        548116631: 'Женя',
        613759219: 'Влад',
        469338261: 'Степан',
        384343953: 'Олег',
        358734682: 'Илья',
        537784508: 'Саша',
        448401733: 'Богдан',
        605903256: 'Леша'
    }

    SCHEDULE_MONDAY_DAYOFF = "\n\nПАР НЕТ"
    SCHEDULE_TUESDAY_DAYOFF = "\n\nПАР НЕТ"
    SCHEDULE_WEDNESDAY_DAYOFF = "\n\nПАР НЕТ"
    SCHEDULE_THURSDAY_DAYOFF = "\n\nПАР НЕТ"
    SCHEDULE_FRIDAY_DAYOFF = "\n\nПАР НЕТ"
    SCHEDULE_SATURDAY_DAYOFF = "\n\nПАР НЕТ"
    SCHEDULE_SUNDAY_DAYOFF = "\n\nПАР НЕТ"

    CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_FULLWEEK = "\n\nпонедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n11:40-13:00 — ООП\n13:05-14:25 — ООП\n\nпятница\n08:30-09:50 — КОМП. СХЕМ.\n10:00-11:20 — КОМП. СХЕМ."
    CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_FULLWEEK = "\n\nпонедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n11:40-13:00 — ООП\n13:05-14:25 — ООП\n\nпятница\n10:00-11:20 — КОМП. СХЕМ.\n13:05-14:25 — КОМП. СХЕМ."
    CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_FULLWEEK = "\n\nпонедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n13:05-14:25 — ООП\n\nпятница\n13:05-14:25 — ООП\n14:30-15:50 — ООП"
    CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_FULLWEEK = "\n\nпонедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n13:05-14:25 — ООП\n\nпятница\n13:05-14:25 — ООП\n14:30-15:50 — ООП"
    CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_FULLWEEK = "\n\nпонедельник\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n11:40-13:00 — ООП\n13:05-14:25 — ООП\n\nпятница\nПАР НЕТ"
    CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_FULLWEEK = "\n\nпонедельник\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n11:40-13:00 — ООП\n13:05-14:25 — ООП\n\nпятница\nПАР НЕТ"
    CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_FULLWEEK = "\n\nпонедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n13:05-14:25 — ООП\n\nпятница\n13:05-14:25 — ООП\n14:30-15:50 — ООП"
    CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_FULLWEEK = "\n\nпонедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n13:05-14:25 — ООП\n\nпятница\n13:05-14:25 — ООП\n14:30-15:50 — ООП"

    CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY = "\n\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ."
    CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY = "\n\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ."
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

    if uid in first_group.keys():
        student_group = "первая группа"
        student_name = first_group[uid] + ", "
    elif uid in second_group.keys():
        student_group = "вторая группа"
        student_name = second_group[uid] + ", "
    else:
        student_group = ""
        student_name = ""
            
    week_template = "\n" + week + " неделя"
    today_template = student_name + student_group + " (" + today + ")"
    yesterday_template = student_name + student_group + " (" + yesterday + ")"
    tomorrow_template = student_name + student_group + " (" + tomorrow + ")"
    monday_template = student_name + student_group + " (понедельник)"
    tuesday_template = student_name + student_group + " (вторник)"
    wednesday_template = student_name + student_group + " (среда)"
    thursday_template = student_name + student_group + " (четверг)"
    friday_template = student_name + student_group + " (пятница)"
    saturday_template = student_name + student_group + " (суббота)"
    sunday_template = student_name + student_group + " (воскресенье)"

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
                if uid in first_group.keys():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
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
                elif uid in second_group.keys():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
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
                if uid in first_group.keys():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
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
                elif uid in second_group.keys():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
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
                if uid in first_group.keys():
                    if date.today().weekday() - 1 == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
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
                elif uid in second_group.keys():
                    if date.today().weekday() - 1 == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
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
                if uid in first_group.keys():
                    if date.today().weekday() + 1 == 7:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
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
                elif uid in second_group.keys():
                    if date.today().weekday() + 1 == 7:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
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
                if uid in first_group.keys():
                    if "понедельник" in msg or "пн" in msg and not any(words in msg for words in monday_tuple):
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, monday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, monday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif "вторник" in msg or "вт" in msg and not any(words in msg for words in tuesday_tuple):
                        bot.send_message(cid, tuesday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif "среда" in msg or "среду" in msg or "ср" in msg and not any(words in msg for words in wednesday_tuple):
                        bot.send_message(cid, wednesday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif "четверг" in msg or "чт" in msg and not any(words in msg for words in thursday_tuple):
                        bot.send_message(cid, thursday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif "пятница" in msg or "пятницу" in msg or "пт" in msg and not any(words in msg for words in friday_tuple):
                        bot.send_message(cid, friday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif "суббота" in msg or "субботу" in msg or "сб" in msg and not any(words in msg for words in saturday_tuple):
                        bot.send_message(cid, saturday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif "воскресенье" in msg or "вс" in msg and not any(words in msg for words in sunday_tuple):
                        bot.send_message(cid, sunday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.keys():
                    if "понедельник" in msg or "пн" in msg and not any(words in msg for words in monday_tuple):
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, monday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, monday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif "вторник" in msg or "вт" in msg and not any(words in msg for words in tuesday_tuple):
                        bot.send_message(cid, tuesday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif "среда" in msg or "среду" in msg or "ср" in msg and not any(words in msg for words in wednesday_tuple):
                        bot.send_message(cid, wednesday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif "четверг" in msg or "чт" in msg and not any(words in msg for words in thursday_tuple):
                        bot.send_message(cid, thursday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif "пятница" in msg or "пятницу" in msg or "пт" in msg and not any(words in msg for words in friday_tuple):
                        bot.send_message(cid, friday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif "суббота" in msg or "субботу" in msg or "сб" in msg and not any(words in msg for words in saturday_tuple):
                        bot.send_message(cid, saturday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif "воскресенье" in msg or "вс" in msg and not any(words in msg for words in sunday_tuple):
                        bot.send_message(cid, sunday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
        if "schedule" in msg:
            if uid in first_group.keys():
                if uid in first_group_eng.keys():
                    bot.send_message(cid, student_group + week_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_FULLWEEK)
                elif uid in second_group_eng.keys():
                    bot.send_message(cid, student_group + week_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_FULLWEEK)
            elif uid in second_group.keys():
                if uid in first_group_eng.keys():
                    bot.send_message(cid, student_group + week_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_FULLWEEK)
                elif uid in second_group_eng.keys():
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
                if uid in first_group.keys():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
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
                elif uid in second_group.keys():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
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
                if uid in first_group.keys():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
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
                elif uid in second_group.keys():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
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
                if uid in first_group.keys():
                    if date.today().weekday() - 1 == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
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
                elif uid in second_group.keys():
                    if date.today().weekday() - 1 == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, yesterday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
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
                if uid in first_group.keys():
                    if date.today().weekday() + 1 == 7:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
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
                elif uid in second_group.keys():
                    if date.today().weekday() + 1 == 7:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, tomorrow_template + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
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
                if uid in first_group.keys():
                    if "понедельник" in msg or "пн" in msg and not any(words in msg for words in monday_tuple):
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, monday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, monday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif "вторник" in msg or "вт" in msg and not any(words in msg for words in tuesday_tuple):
                        bot.send_message(cid, tuesday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif "среда" in msg or "среду" in msg or "ср" in msg and not any(words in msg for words in wednesday_tuple):
                        bot.send_message(cid, wednesday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif "четверг" in msg or "чт" in msg and not any(words in msg for words in thursday_tuple):
                        bot.send_message(cid, thursday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif "пятница" in msg or "пятницу" in msg or "пт" in msg and not any(words in msg for words in friday_tuple):
                        bot.send_message(cid, friday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif "суббота" in msg or "субботу" in msg or "сб" in msg and not any(words in msg for words in saturday_tuple):
                        bot.send_message(cid, saturday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif "воскресенье" in msg or "вс" in msg and not any(words in msg for words in sunday_tuple):
                        bot.send_message(cid, sunday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.keys():
                    if "понедельник" in msg or "пн" in msg and not any(words in msg for words in monday_tuple):
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, monday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, monday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif "вторник" in msg or "вт" in msg and not any(words in msg for words in tuesday_tuple):
                        bot.send_message(cid, tuesday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif "среда" in msg or "среду" in msg or "ср" in msg and not any(words in msg for words in wednesday_tuple):
                        bot.send_message(cid, wednesday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif "четверг" in msg or "чт" in msg and not any(words in msg for words in thursday_tuple):
                        bot.send_message(cid, thursday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif "пятница" in msg or "пятницу" in msg or "пт" in msg and not any(words in msg for words in friday_tuple):
                        bot.send_message(cid, friday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif "суббота" in msg or "субботу" in msg or "сб" in msg and not any(words in msg for words in saturday_tuple):
                        bot.send_message(cid, saturday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif "воскресенье" in msg or "вс" in msg and not any(words in msg for words in sunday_tuple):
                        bot.send_message(cid, sunday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
        if "schedule" in msg:
            if uid in first_group.keys():
                if uid in first_group_eng.keys():
                    bot.send_message(cid, student_group + week_template + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_FULLWEEK)
                elif uid in second_group_eng.keys():
                    bot.send_message(cid, student_group + week_template + CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_FULLWEEK)
            elif uid in second_group.keys():
                if uid in first_group_eng.keys():
                    bot.send_message(cid, student_group + week_template + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_FULLWEEK)
                elif uid in second_group_eng.keys():
                    bot.send_message(cid, student_group + week_template + CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_FULLWEEK)
            else:
                bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)

@app.route('/'+ TOKEN, methods=['POST'])
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

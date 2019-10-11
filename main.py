import flask, os, telebot, time, logging, random
from flask import Flask, request
from telebot import types
from datetime import date, timedelta
from random import randrange

token = '642122532:AAGKg4s2_ffJqDNTrqvbI7-qeFRxNEOBPV8'
bot = telebot.TeleBot(token, threaded=False)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "привет, чем могу быть полезен?")

@bot.message_handler(content_types=['text'])
def predefined_commands(message):
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
        ('Виталий'): 548116631,
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

    weeknum = date.today().isocalendar()[1]
    message.text = message.text.lower()
    meme_url = str("https://t.me/mnekovtoroi/" + str(random.randint(7, 4687)))

    if (weeknum % 2) == 0:
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

    for name, identifier in all_students.items():
        if identifier == message.from_user.id:
            student_name = name.lower()
    for name, identifier in first_group.items():
        if identifier == message.from_user.id:
            student_group = "первая"
    for name, identifier in second_group.items():
        if identifier == message.from_user.id:
            student_group = "вторая"
    if message.from_user.id in all_students.values():
        if "мем" in message.text or "meme" in message.text:
            bot.send_photo(message.chat.id, meme_url)
    else:
        bot.send_message(message.chat.id, "мы ещё не знакомы, напиши мне в личку что-нибудь", reply_to_message_id=message.message_id)

    week_template = " группа" + " / " + week + " неделя"
    today_template = student_name + ", " + student_group + " группа" + " (" + today + ")"
    yesterday_template = student_name + ", " + student_group + " группа" + " (" + yesterday + ")"
    tomorrow_template = student_name + ", " + student_group + " группа" + " (" + tomorrow + ")"
    monday_template = student_name + ", " + student_group + " группа" + " (понедельник)"
    tuesday_template = student_name + ", " + student_group + " группа" + " (вторник)"
    wednesday_template = student_name + ", " + student_group + " группа" + " (среда)"
    thursday_template = student_name + ", " + student_group + " группа" + " (четверг)"
    friday_template = student_name + ", " + student_group + " группа" + " (пятница)"
    saturday_template = student_name + ", " + student_group + " группа" + " (суббота)"
    sunday_template = student_name + ", " + student_group + " группа" + " (воскресенье)"

    classes_tuple = "пары", "парам", "расписание", "расписанию", "предметы", "предметам"
    day_tuple = "какой день", "какой сейчас день", "какой сегодня день"
    days_tuple = "сегодня", "вчера", "завтра"
    week_tuple = "какая неделя", "какая сейчас неделя", "какая сегодня неделя"
    weekdays_tuple = "понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье", "среду", "пятницу", "субботу", "пн", "вт", "ср", "чт", "пт", "сб", "вс"
    today_tuple = "вчера", "завтра"
    yesterday_tuple = "сегодня", "завтра"
    tomorrow_tuple = "вчера", "сегодня"
    monday_tuple = "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье", "среду", "пятницу", "субботу", "пн", "вт", "ср", "чт", "пт", "сб", "вс"
    tuesday_tuple = "понедельник", "среда", "четверг", "пятница", "суббота", "воскресенье", "среду", "пятницу", "субботу", "пн", "ср", "чт", "пт", "сб", "вс"
    wednesday_tuple = "понедельник", "вторник", "четверг", "пятница", "суббота", "воскресенье", "пятницу", "субботу", "пн", "вт", "чт", "пт", "сб", "вс"
    thursday_tuple = "понедельник", "вторник", "среда", "пятница", "суббота", "воскресенье", "среду", "пятницу", "субботу", "пн", "вт", "ср", "пт", "сб", "вс"
    friday_tuple = "понедельник", "вторник", "среда", "четверг", "суббота", "воскресенье", "среду", "субботу", "пн", "вт", "ср", "чт", "сб", "вс"
    saturday_tuple = "понедельник", "вторник", "среда", "четверг", "пятница", "воскресенье", "среду", "пятницу", "пн", "вт", "ср", "чт", "пт", "вс"
    sunday_tuple = "понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "среду", "пятницу", "субботу", "пн", "вт", "ср", "чт", "пт", "сб"

    if any(words in message.text for words in week_tuple):
        bot.send_message(message.chat.id, "сейчас " + week + " неделя", reply_to_message_id=message.message_id)

    if weekorder == True:
        if date.today().weekday() == 0 and any(words in message.text for words in day_tuple):
            bot.send_message(message.chat.id, "сегодня светлый " + today, reply_to_message_id=message.message_id)
        elif date.today().weekday() == 1 and any(words in message.text for words in day_tuple):
            bot.send_message(message.chat.id, "сегодня светлый " + today, reply_to_message_id=message.message_id)
        elif date.today().weekday() == 2 and any(words in message.text for words in day_tuple):
            bot.send_message(message.chat.id, "сегодня светлая " + today, reply_to_message_id=message.message_id)
        elif date.today().weekday() == 3 and any(words in message.text for words in day_tuple):
            bot.send_message(message.chat.id, "сегодня светлый " + today, reply_to_message_id=message.message_id)
        elif date.today().weekday() == 4 and any(words in message.text for words in day_tuple):
            bot.send_message(message.chat.id, "сегодня светлая " + today, reply_to_message_id=message.message_id)
        elif date.today().weekday() == 5 and any(words in message.text for words in day_tuple):
            bot.send_message(message.chat.id, "сегодня светлая " + today, reply_to_message_id=message.message_id)
        elif date.today().weekday() == 6 and any(words in message.text for words in day_tuple):
            bot.send_message(message.chat.id, "сегодня светлое " + today, reply_to_message_id=message.message_id)
        elif "schedule" in message.text:
            if message.from_user.id in first_group.values():
                if message.from_user.id in first_group_eng.values():
                    bot.send_message(message.chat.id, student_group + week_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_FULLWEEK)
                elif message.from_user.id in second_group_eng.values():
                    bot.send_message(message.chat.id, student_group + week_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_FULLWEEK)
            elif message.from_user.id in second_group.values():
                if message.from_user.id in first_group_eng.values():
                    bot.send_message(message.chat.id, student_group + week_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_FULLWEEK)
                elif message.from_user.id in second_group_eng.values():
                    bot.send_message(message.chat.id, student_group + week_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_FULLWEEK)
            elif message.from_user.id not in all_students.values():
                bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id=message.message_id)
        elif any(words in message.text for words in classes_tuple):
            if not any(words in message.text for words in days_tuple) and not any(words in message.text for words in weekdays_tuple):
                if message.from_user.id in first_group.values():
                    if date.today().weekday() == 0:
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 1:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 2:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 3:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 4:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id in second_group.values():
                    if date.today().weekday() == 0:
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 1:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 2:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 3:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 4:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id not in all_students.values():
                    bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id=message.message_id)
            elif "сегодня" in message.text and not any(words in message.text for words in today_tuple):
                if message.from_user.id in first_group.values():
                    if date.today().weekday() == 0:
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 1:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 2:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 3:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 4:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id in second_group.values():
                    if date.today().weekday() == 0:
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 1:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 2:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 3:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 4:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id not in all_students.values():
                    bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id=message.message_id)
            elif "вчера" in message.text and not any(words in message.text for words in yesterday_tuple):
                if message.from_user.id in first_group.values():
                    if date.today().weekday() - 1 == 0:
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 1:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 2:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 3:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 4:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 5:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 6:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id in second_group.values():
                    if date.today().weekday() - 1 == 0:
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 1:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 2:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 3:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 4:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 5:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 6:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id not in all_students.values():
                    bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id=message.message_id)
            elif "завтра" in message.text and not any(words in message.text for words in tomorrow_tuple):
                if message.from_user.id in first_group.values():
                    if date.today().weekday() + 1 == 7:
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 1:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 2:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 3:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 4:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 5:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 6:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id in second_group.values():
                    if date.today().weekday() + 1 == 7:
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 1:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 2:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 3:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 4:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 5:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 6:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id not in all_students.values():
                    bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id=message.message_id)
            elif not any(words in message.text for words in days_tuple):
                if message.from_user.id in first_group.values():
                    if "понедельник" in message.text or "пн" in message.text and not any(words in message.text for words in monday_tuple):
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, monday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, monday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif "вторник" in message.text or "вт" in message.text and not any(words in message.text for words in tuesday_tuple):
                        bot.send_message(message.chat.id, tuesday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif "среда" in message.text or "среду" in message.text or "ср" in message.text and not any(words in message.text for words in wednesday_tuple):
                        bot.send_message(message.chat.id, wednesday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif "четверг" in message.text or "чт" in message.text and not any(words in message.text for words in thursday_tuple):
                        bot.send_message(message.chat.id, thursday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif "пятница" in message.text or "пятницу" in message.text or "пт" in message.text and not any(words in message.text for words in friday_tuple):
                        bot.send_message(message.chat.id, friday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=message.message_id)
                    elif "суббота" in message.text or "субботу" in message.text or "сб" in message.text and not any(words in message.text for words in saturday_tuple):
                        bot.send_message(message.chat.id, saturday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY, reply_to_message_id=message.message_id)
                    elif "воскресенье" in message.text or "вс" in message.text and not any(words in message.text for words in sunday_tuple):
                        bot.send_message(message.chat.id, sunday_template + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id in second_group.values():
                    if "понедельник" in message.text or "пн" in message.text and not any(words in message.text for words in monday_tuple):
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, monday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, monday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif "вторник" in message.text or "вт" in message.text and not any(words in message.text for words in tuesday_tuple):
                        bot.send_message(message.chat.id, tuesday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif "среда" in message.text or "среду" in message.text or "ср" in message.text and not any(words in message.text for words in wednesday_tuple):
                        bot.send_message(message.chat.id, wednesday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif "четверг" in message.text or "чт" in message.text and not any(words in message.text for words in thursday_tuple):
                        bot.send_message(message.chat.id, thursday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif "пятница" in message.text or "пятницу" in message.text or "пт" in message.text and not any(words in message.text for words in friday_tuple):
                        bot.send_message(message.chat.id, friday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=message.message_id)
                    elif "суббота" in message.text or "субботу" in message.text or "сб" in message.text and not any(words in message.text for words in saturday_tuple):
                        bot.send_message(message.chat.id, saturday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY, reply_to_message_id=message.message_id)
                    elif "воскресенье" in message.text or "вс" in message.text and not any(words in message.text for words in sunday_tuple):
                        bot.send_message(message.chat.id, sunday_template + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id not in all_students.values():
                    bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id=message.message_id)
    elif weekorder == False:
        if date.today().weekday() == 0 and any(words in message.text for words in day_tuple):
            bot.send_message(message.chat.id, "сегодня тёмный " + today, reply_to_message_id=message.message_id)
        elif date.today().weekday() == 1 and any(words in message.text for words in day_tuple):
            bot.send_message(message.chat.id, "сегодня тёмный " + today, reply_to_message_id=message.message_id)
        elif date.today().weekday() == 2 and any(words in message.text for words in day_tuple):
            bot.send_message(message.chat.id, "сегодня тёмная " + today, reply_to_message_id=message.message_id)
        elif date.today().weekday() == 3 and any(words in message.text for words in day_tuple):
            bot.send_message(message.chat.id, "сегодня тёмный " + today, reply_to_message_id=message.message_id)
        elif date.today().weekday() == 4 and any(words in message.text for words in day_tuple):
            bot.send_message(message.chat.id, "сегодня тёмная " + today, reply_to_message_id=message.message_id)
        elif date.today().weekday() == 5 and any(words in message.text for words in day_tuple):
            bot.send_message(message.chat.id, "сегодня тёмная " + today, reply_to_message_id=message.message_id)
        elif date.today().weekday() == 6 and any(words in message.text for words in day_tuple):
            bot.send_message(message.chat.id, "сегодня тёмное " + today, reply_to_message_id=message.message_id)
        if "schedule" in message.text:
            if message.from_user.id in first_group.values():
                if message.from_user.id in first_group_eng.values():
                    bot.send_message(message.chat.id, student_group + week_template + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_FULLWEEK)
                elif message.from_user.id in second_group_eng.values():
                    bot.send_message(message.chat.id, student_group + week_template + CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_FULLWEEK)
            elif message.from_user.id in second_group.values():
                if message.from_user.id in first_group_eng.values():
                    bot.send_message(message.chat.id, student_group + week_template + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_FULLWEEK)
                elif message.from_user.id in second_group_eng.values():
                    bot.send_message(message.chat.id, student_group + week_template + CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_FULLWEEK)
            elif message.from_user.id not in all_students.values():
                bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id=message.message_id)
        if any(words in message.text for words in classes_tuple):
            if not any(words in message.text for words in days_tuple) and not any(words in message.text for words in weekdays_tuple):
                if message.from_user.id in first_group.values():
                    if date.today().weekday() == 0 and not any(words in message.text for words in day_tuple):
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 1 and not any(words in message.text for words in day_tuple):
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 2 and not any(words in message.text for words in day_tuple):
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 3 and not any(words in message.text for words in day_tuple):
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 4 and not any(words in message.text for words in day_tuple):
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id in second_group.values():
                    if date.today().weekday() == 0 and not any(words in message.text for words in day_tuple):
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 1 and not any(words in message.text for words in day_tuple):
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 2 and not any(words in message.text for words in day_tuple):
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 3 and not any(words in message.text for words in day_tuple):
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 4 and not any(words in message.text for words in day_tuple):
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id not in all_students.values():
                    bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id=message.message_id)
            elif "сегодня" in message.text and not any(words in message.text for words in today_tuple):
                if message.from_user.id in first_group.values():
                    if date.today().weekday() == 0:
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 1:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 2:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 3:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 4:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id in second_group.values():
                    if date.today().weekday() == 0:
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 1:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 2:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 3:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() == 4:
                        bot.send_message(message.chat.id, today_template + CS18_SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id not in all_students.values():
                    bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id=message.message_id)
            if "вчера" in message.text and not any(words in message.text for words in yesterday_tuple):
                if message.from_user.id in first_group.values():
                    if date.today().weekday() - 1 == 0:
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 1:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 2:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 3:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 4:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 5:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_SATURDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 6:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_SUNDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id in second_group.values():
                    if date.today().weekday() - 1 == 0:
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 1:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 2:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 3:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 4:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 5:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_SATURDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() - 1 == 6:
                        bot.send_message(message.chat.id, yesterday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_SUNDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id not in all_students.values():
                    bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id=message.message_id)
            elif "завтра" in message.text and not any(words in message.text for words in tomorrow_tuple):
                if message.from_user.id in first_group.values():
                    if date.today().weekday() + 1 == 7:
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 1:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 2:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 3:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 4:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 5:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_DARKWEEK_1GROUP_SATURDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 6:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_DARKWEEK_1GROUP_SUNDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id in second_group.values():
                    if date.today().weekday() + 1 == 7:
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 1:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 2:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_DARKWEEK_2GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 3:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 4:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 5:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_DARKWEEK_2GROUP_SATURDAY, reply_to_message_id=message.message_id)
                    elif date.today().weekday() + 1 == 6:
                        bot.send_message(message.chat.id, tomorrow_template + CS18_SCHEDULE_DARKWEEK_2GROUP_SUNDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id not in all_students.values():
                    bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id=message.message_id)
            elif not any(words in message.text for words in days_tuple):
                if message.from_user.id in first_group.values():
                    if "понедельник" in message.text or "пн" in message.text and not any(words in message.text for words in monday_tuple):
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, monday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, monday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif "вторник" in message.text or "вт" in message.text and not any(words in message.text for words in tuesday_tuple):
                        bot.send_message(message.chat.id, tuesday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif "среда" in message.text or "среду" in message.text or "ср" in message.text and not any(words in message.text for words in wednesday_tuple):
                        bot.send_message(message.chat.id, wednesday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif "четверг" in message.text or "чт" in message.text and not any(words in message.text for words in thursday_tuple):
                        bot.send_message(message.chat.id, thursday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif "пятница" in message.text or "пятницу" in message.text or "пт" in message.text and not any(words in message.text for words in friday_tuple):
                        bot.send_message(message.chat.id, friday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=message.message_id)
                    elif "суббота" in message.text or "субботу" in message.text or "сб" in message.text and not any(words in message.text for words in saturday_tuple):
                        bot.send_message(message.chat.id, saturday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_SATURDAY, reply_to_message_id=message.message_id)
                    elif "воскресенье" in message.text or "вс" in message.text and not any(words in message.text for words in sunday_tuple):
                        bot.send_message(message.chat.id, sunday_template + CS18_SCHEDULE_DARKWEEK_1GROUP_SUNDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id in second_group.values():
                    if "понедельник" in message.text or "пн" in message.text and not any(words in message.text for words in monday_tuple):
                        if message.from_user.id in first_group_eng.values():
                            bot.send_message(message.chat.id, monday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                        elif message.from_user.id in second_group_eng.values():
                            bot.send_message(message.chat.id, monday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=message.message_id)
                    elif "вторник" in message.text or "вт" in message.text and not any(words in message.text for words in tuesday_tuple):
                        bot.send_message(message.chat.id, tuesday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=message.message_id)
                    elif "среда" in message.text or "среду" in message.text or "ср" in message.text and not any(words in message.text for words in wednesday_tuple):
                        bot.send_message(message.chat.id, wednesday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_WEDNESDAY, reply_to_message_id=message.message_id)
                    elif "четверг" in message.text or "чт" in message.text and not any(words in message.text for words in thursday_tuple):
                        bot.send_message(message.chat.id, thursday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=message.message_id)
                    elif "пятница" in message.text or "пятницу" in message.text or "пт" in message.text and not any(words in message.text for words in friday_tuple):
                        bot.send_message(message.chat.id, friday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=message.message_id)
                    elif "суббота" in message.text or "субботу" in message.text or "сб" in message.text and not any(words in message.text for words in saturday_tuple):
                        bot.send_message(message.chat.id, saturday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_SATURDAY, reply_to_message_id=message.message_id)
                    elif "воскресенье" in message.text or "вс" in message.text and not any(words in message.text for words in sunday_tuple):
                        bot.send_message(message.chat.id, sunday_template + CS18_SCHEDULE_DARKWEEK_2GROUP_SUNDAY, reply_to_message_id=message.message_id)
                elif message.from_user.id not in all_students.values():
                    bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id=message.message_id)

bot.polling(none_stop=True)

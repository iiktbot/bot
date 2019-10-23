import telebot
from telebot import types

TOKEN = os.environ["TOKEN"]
bot = telebot.TeleBot(TOKEN, threaded=False)

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

    global first_group
    global second_group
    global first_group_eng
    global second_group_eng

    global SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_FULLWEEK
    global SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_FULLWEEK
    global SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_FULLWEEK
    global SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_FULLWEEK
    global SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_FULLWEEK
    global SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_FULLWEEK
    global SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_FULLWEEK
    global SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_FULLWEEK

    global SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY
    global SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY
    global SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY
    global SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY
    global SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY
    global SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY
    global SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY
    global SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY

    global SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY
    global SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY
    global SCHEDULE_DARKWEEK_1GROUP_TUESDAY
    global SCHEDULE_DARKWEEK_2GROUP_TUESDAY

    global SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY
    global SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY
    global SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY
    global SCHEDULE_DARKWEEK_2GROUP_WEDNESDAY

    global SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY
    global SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY
    global SCHEDULE_DARKWEEK_1GROUP_THURSDAY
    global SCHEDULE_DARKWEEK_2GROUP_THURSDAY

    global SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY
    global SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY
    global SCHEDULE_DARKWEEK_1GROUP_FRIDAY
    global SCHEDULE_DARKWEEK_2GROUP_FRIDAY

    global SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY
    global SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY
    global SCHEDULE_DARKWEEK_1GROUP_SATURDAY
    global SCHEDULE_DARKWEEK_2GROUP_SATURDAY

    global SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY
    global SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY
    global SCHEDULE_DARKWEEK_1GROUP_SUNDAY
    global SCHEDULE_DARKWEEK_2GROUP_SUNDAY

    SCHEDULE_MONDAY_DAYOFF = "\n\nПАР НЕТ"
    SCHEDULE_TUESDAY_DAYOFF = "\n\nПАР НЕТ"
    SCHEDULE_WEDNESDAY_DAYOFF = "\n\nПАР НЕТ"
    SCHEDULE_THURSDAY_DAYOFF = "\n\nПАР НЕТ"
    SCHEDULE_FRIDAY_DAYOFF = "\n\nПАР НЕТ"
    SCHEDULE_SATURDAY_DAYOFF = "\n\nПАР НЕТ"
    SCHEDULE_SUNDAY_DAYOFF = "\n\nПАР НЕТ"

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
    if uid in second_group.keys():
        student_group = "вторая группа"
        student_name = second_group[uid] + ", "

    week_template = " группа / " + week + " неделя"
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
        if any(words in msg for words in week_tuple):
            bot.send_message(cid, "сейчас " + week + " неделя", reply_to_message_id=mid)
        if any(words in msg for words in classes_tuple):
            if not any(words in msg for words in days_tuple) and not any(words in msg for words in weekdays_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.keys():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 1:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 2:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 3:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 4:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 5:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 6:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.keys():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 1:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 2:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 3:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 4:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 5:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 6:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
            elif "сегодня" in msg and not any(words in msg for words in today_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.keys():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 1:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 2:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 3:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 4:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 5:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 6:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.keys():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 1:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 2:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 3:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 4:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 5:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 6:
                        bot.send_message(cid, today_template + SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
            elif "вчера" in msg and not any(words in msg for words in yesterday_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.keys():
                    if date.today().weekday() - 1 == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, yesterday_template + SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, yesterday_template + SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 1:
                        bot.send_message(cid, yesterday_template + SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 2:
                        bot.send_message(cid, yesterday_template + SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 3:
                        bot.send_message(cid, yesterday_template + SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 4:
                        bot.send_message(cid, yesterday_template + SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 5:
                        bot.send_message(cid, yesterday_template + SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 6:
                        bot.send_message(cid, yesterday_template + SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.keys():
                    if date.today().weekday() - 1 == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, yesterday_template + SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, yesterday_template + SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 1:
                        bot.send_message(cid, yesterday_template + SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 2:
                        bot.send_message(cid, yesterday_template + SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 3:
                        bot.send_message(cid, yesterday_template + SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 4:
                        bot.send_message(cid, yesterday_template + SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 5:
                        bot.send_message(cid, yesterday_template + SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 6:
                        bot.send_message(cid, yesterday_template + SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
            elif "завтра" in msg and not any(words in msg for words in tomorrow_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.keys():
                    if date.today().weekday() + 1 == 7:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, tomorrow_template + SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, tomorrow_template + SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 1:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 2:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 3:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 4:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 5:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 6:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.keys():
                    if date.today().weekday() + 1 == 7:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, tomorrow_template + SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, tomorrow_template + SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 1:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 2:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 3:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 4:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 5:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 6:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
            elif not any(words in msg for words in days_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.keys():
                    if "понедельник" in msg or "пн" in msg and not any(words in msg for words in monday_tuple):
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, monday_template + SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, monday_template + SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif "вторник" in msg or "вт" in msg and not any(words in msg for words in tuesday_tuple):
                        bot.send_message(cid, tuesday_template + SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif "среда" in msg or "среду" in msg or "ср" in msg and not any(words in msg for words in wednesday_tuple):
                        bot.send_message(cid, wednesday_template + SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif "четверг" in msg or "чт" in msg and not any(words in msg for words in thursday_tuple):
                        bot.send_message(cid, thursday_template + SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif "пятница" in msg or "пятницу" in msg or "пт" in msg and not any(words in msg for words in friday_tuple):
                        bot.send_message(cid, friday_template + SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif "суббота" in msg or "субботу" in msg or "сб" in msg and not any(words in msg for words in saturday_tuple):
                        bot.send_message(cid, saturday_template + SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif "воскресенье" in msg or "вс" in msg and not any(words in msg for words in sunday_tuple):
                        bot.send_message(cid, sunday_template + SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.keys():
                    if "понедельник" in msg or "пн" in msg and not any(words in msg for words in monday_tuple):
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, monday_template + SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, monday_template + SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif "вторник" in msg or "вт" in msg and not any(words in msg for words in tuesday_tuple):
                        bot.send_message(cid, tuesday_template + SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif "среда" in msg or "среду" in msg or "ср" in msg and not any(words in msg for words in wednesday_tuple):
                        bot.send_message(cid, wednesday_template + SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif "четверг" in msg or "чт" in msg and not any(words in msg for words in thursday_tuple):
                        bot.send_message(cid, thursday_template + SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif "пятница" in msg or "пятницу" in msg or "пт" in msg and not any(words in msg for words in friday_tuple):
                        bot.send_message(cid, friday_template + SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif "суббота" in msg or "субботу" in msg or "сб" in msg and not any(words in msg for words in saturday_tuple):
                        bot.send_message(cid, saturday_template + SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif "воскресенье" in msg or "вс" in msg and not any(words in msg for words in sunday_tuple):
                        bot.send_message(cid, sunday_template + SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
        if "schedule" in msg:
            if uid in first_group.keys():
                if uid in first_group_eng.keys():
                    bot.send_message(cid, student_group + week_template + SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_FULLWEEK)
                elif uid in second_group_eng.keys():
                    bot.send_message(cid, student_group + week_template + SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_FULLWEEK)
            elif uid in second_group.keys():
                if uid in first_group_eng.keys():
                    bot.send_message(cid, student_group + week_template + SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_FULLWEEK)
                elif uid in second_group_eng.keys():
                    bot.send_message(cid, student_group + week_template + SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_FULLWEEK)
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
                            bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 1:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 2:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 3:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 4:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 5:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 6:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.keys():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 1:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 2:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 3:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 4:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 5:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 6:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
            elif "сегодня" in msg and not any(words in msg for words in today_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.keys():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 1:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 2:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 3:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 4:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 5:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 6:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.keys():
                    if date.today().weekday() == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 1:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 2:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 3:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 4:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 5:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() == 6:
                        bot.send_message(cid, today_template + SCHEDULE_DARKWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
            elif "вчера" in msg and not any(words in msg for words in yesterday_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.keys():
                    if date.today().weekday() - 1 == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, yesterday_template + SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, yesterday_template + SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 1:
                        bot.send_message(cid, yesterday_template + SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 2:
                        bot.send_message(cid, yesterday_template + SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 3:
                        bot.send_message(cid, yesterday_template + SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 4:
                        bot.send_message(cid, yesterday_template + SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 5:
                        bot.send_message(cid, yesterday_template + SCHEDULE_DARKWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 6:
                        bot.send_message(cid, yesterday_template + SCHEDULE_DARKWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.keys():
                    if date.today().weekday() - 1 == 0:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, yesterday_template + SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, yesterday_template + SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 1:
                        bot.send_message(cid, yesterday_template + SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 2:
                        bot.send_message(cid, yesterday_template + SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 3:
                        bot.send_message(cid, yesterday_template + SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 4:
                        bot.send_message(cid, yesterday_template + SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 5:
                        bot.send_message(cid, yesterday_template + SCHEDULE_DARKWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() - 1 == 6:
                        bot.send_message(cid, yesterday_template + SCHEDULE_DARKWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
            elif "завтра" in msg and not any(words in msg for words in tomorrow_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.keys():
                    if date.today().weekday() + 1 == 7:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, tomorrow_template + SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, tomorrow_template + SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 1:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 2:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 3:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 4:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 5:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_DARKWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 6:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_DARKWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.keys():
                    if date.today().weekday() + 1 == 7:
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, tomorrow_template + SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, tomorrow_template + SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 1:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 2:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_DARKWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 3:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 4:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 5:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_DARKWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif date.today().weekday() + 1 == 6:
                        bot.send_message(cid, tomorrow_template + SCHEDULE_DARKWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
            elif not any(words in msg for words in days_tuple) and not any(words in msg for words in exceptions_tuple):
                if uid in first_group.keys():
                    if "понедельник" in msg or "пн" in msg and not any(words in msg for words in monday_tuple):
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, monday_template + SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, monday_template + SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif "вторник" in msg or "вт" in msg and not any(words in msg for words in tuesday_tuple):
                        bot.send_message(cid, tuesday_template + SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=mid)
                    elif "среда" in msg or "среду" in msg or "ср" in msg and not any(words in msg for words in wednesday_tuple):
                        bot.send_message(cid, wednesday_template + SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif "четверг" in msg or "чт" in msg and not any(words in msg for words in thursday_tuple):
                        bot.send_message(cid, thursday_template + SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=mid)
                    elif "пятница" in msg or "пятницу" in msg or "пт" in msg and not any(words in msg for words in friday_tuple):
                        bot.send_message(cid, friday_template + SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=mid)
                    elif "суббота" in msg or "субботу" in msg or "сб" in msg and not any(words in msg for words in saturday_tuple):
                        bot.send_message(cid, saturday_template + SCHEDULE_DARKWEEK_1GROUP_SATURDAY, reply_to_message_id=mid)
                    elif "воскресенье" in msg or "вс" in msg and not any(words in msg for words in sunday_tuple):
                        bot.send_message(cid, sunday_template + SCHEDULE_DARKWEEK_1GROUP_SUNDAY, reply_to_message_id=mid)
                elif uid in second_group.keys():
                    if "понедельник" in msg or "пн" in msg and not any(words in msg for words in monday_tuple):
                        if uid in first_group_eng.keys():
                            bot.send_message(cid, monday_template + SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid)
                        elif uid in second_group_eng.keys():
                            bot.send_message(cid, monday_template + SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid)
                    elif "вторник" in msg or "вт" in msg and not any(words in msg for words in tuesday_tuple):
                        bot.send_message(cid, tuesday_template + SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=mid)
                    elif "среда" in msg or "среду" in msg or "ср" in msg and not any(words in msg for words in wednesday_tuple):
                        bot.send_message(cid, wednesday_template + SCHEDULE_DARKWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid)
                    elif "четверг" in msg or "чт" in msg and not any(words in msg for words in thursday_tuple):
                        bot.send_message(cid, thursday_template + SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=mid)
                    elif "пятница" in msg or "пятницу" in msg or "пт" in msg and not any(words in msg for words in friday_tuple):
                        bot.send_message(cid, friday_template + SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=mid)
                    elif "суббота" in msg or "субботу" in msg or "сб" in msg and not any(words in msg for words in saturday_tuple):
                        bot.send_message(cid, saturday_template + SCHEDULE_DARKWEEK_2GROUP_SATURDAY, reply_to_message_id=mid)
                    elif "воскресенье" in msg or "вс" in msg and not any(words in msg for words in sunday_tuple):
                        bot.send_message(cid, sunday_template + SCHEDULE_DARKWEEK_2GROUP_SUNDAY, reply_to_message_id=mid)
                else:
                    bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)
        if "schedule" in msg:
            if uid in first_group.keys():
                if uid in first_group_eng.keys():
                    bot.send_message(cid, student_group + week_template + SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_FULLWEEK)
                elif uid in second_group_eng.keys():
                    bot.send_message(cid, student_group + week_template + SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_FULLWEEK)
            elif uid in second_group.keys():
                if uid in first_group_eng.keys():
                    bot.send_message(cid, student_group + week_template + SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_FULLWEEK)
                elif uid in second_group_eng.keys():
                    bot.send_message(cid, student_group + week_template + SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_FULLWEEK)
            else:
                bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)

    meme_url = str("https://t.me/LaQeque/" + str(random.randint(5, 39946)))
    meme_req = requests.get(meme_url)

    if "мем" in msg or "meme" in msg:
        if uid in first_group.keys() or uid in second_group.keys():
            bot.send_chat_action(cid, "upload_photo")
            bot.send_photo(cid, meme_url)
        else:
            bot.send_message(cid, "вряд ли ты здесь учишься", reply_to_message_id=mid)

@bot.message_handler(content_types=['sticker'])
def predefined_stickers(message):
    global first_group
    global second_group
    global first_group_eng
    global second_group_eng

    cid = message.chat.id
    uid = message.from_user.id

    sticker_rnm = random.randint(1, 25)

    if sticker_rnm == 1:
        sid = "CAADAgADNwADTV8oGAcnDK_zzifQFgQ"
    elif sticker_rnm == 2:
        sid = "CAADAgADOAADTV8oGIkHWmw4--6sFgQ"
    elif sticker_rnm == 3:
        sid = "CAADAgADOQADTV8oGB0jpTwBtJ3qFgQ"
    elif sticker_rnm == 4:
        sid = "CAADAgADOgADTV8oGMRKEjeYMD-iFgQ"
    elif sticker_rnm == 5:
        sid = "CAADAgADOwADTV8oGPYpjAugj5MkFgQ"
    elif sticker_rnm == 6:
        sid = "CAADAgADPAADTV8oGNHRaGn8VRqSFgQ"
    elif sticker_rnm == 7:
        sid = "CAADAgADPQADTV8oGGv7CE-jUh8EFgQ"
    elif sticker_rnm == 8:
        sid = "CAADAgADPwADTV8oGGEa15DV51VsFgQ"
    elif sticker_rnm == 9:
        sid = "CAADAgADQQADTV8oGHxIB3e9wuKQFgQ"
    elif sticker_rnm == 10:
        sid = "CAADAgADQgADTV8oGOKRYZfYhYJFFgQ"
    elif sticker_rnm == 11:
        sid = "CAADAgADQwADTV8oGE78wiPH81acFgQ"
    elif sticker_rnm == 12:
        sid = "CAADAgADRAADTV8oGAtV7hSpVNtaFgQ"
    elif sticker_rnm == 13:
        sid = "CAADAgADRQADTV8oGFslQVK175XIFgQ"
    elif sticker_rnm == 14:
        sid = "CAADAgADRgADTV8oGNfQA4YP9hbGFgQ"
    elif sticker_rnm == 15:
        sid = "CAADAgADRwADTV8oGE_kCZ6bNeYWFgQ"
    elif sticker_rnm == 16:
        sid = "CAADAgADSAADTV8oGAW7JHvjQFXFFgQ"
    elif sticker_rnm == 17:
        sid = "CAADAgADSQADTV8oGJ2B3Lds1bOCFgQ"
    elif sticker_rnm == 18:
        sid = "CAADAgADSgADTV8oGM58vpLz3FuoFgQ"
    elif sticker_rnm == 19:
        sid = "CAADAgADSwADTV8oGOxJeXJbuuKHFgQ"
    elif sticker_rnm == 20:
        sid = "CAADAgADTQADTV8oGLiiZvA26ikuFgQ"
    elif sticker_rnm == 21:
        sid = "CAADAgADTAADTV8oGJhTCjwdw5EYFgQ"
    elif sticker_rnm == 22:
        sid = "CAADAgADTwADTV8oGJzFxvw-eMa5FgQ"
    elif sticker_rnm == 23:
        sid = "CAADAgADTgADTV8oGOMvW5CjVqGhFgQ"
    elif sticker_rnm == 24:
        sid = "CAADAgADUAADTV8oGMB0LsS6SDJtFgQ"
    elif sticker_rnm == 25:
        sid = "CAADAgADUQADTV8oGM5oZrUGiKN-FgQ"

    if uid in first_group.keys() or uid in second_group.keys():
        bot.send_sticker(cid, sid)

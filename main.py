#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask, telebot, os, requests, datetime, time, random, re, psycopg2
from flask import Flask, request
from telebot import types
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta, MO, TU, WE, TH, FR, SA, SU
from random import randrange

TOKEN = os.environ['TOKEN']
DATABASE_URL = os.environ['DATABASE_URL']

bot = telebot.TeleBot(TOKEN, skip_pending=True, threaded=False)
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
app = Flask(__name__)

SCHEDULE_MONDAY_DAYOFF = 'ПАР НЕТ'
SCHEDULE_TUESDAY_DAYOFF = 'ПАР НЕТ'
SCHEDULE_WEDNESDAY_DAYOFF = 'ПАР НЕТ'
SCHEDULE_THURSDAY_DAYOFF = 'ПАР НЕТ'
SCHEDULE_FRIDAY_DAYOFF = 'ПАР НЕТ'
SCHEDULE_SATURDAY_DAYOFF = 'ПАР НЕТ'
SCHEDULE_SUNDAY_DAYOFF = 'ПАР НЕТ'

CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_FULLWEEK = 'понедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n11:40-13:00 — ООП\n13:05-14:25 — ООП\n\nпятница\n08:30-09:50 — КОМП. СХЕМ.\n10:00-11:20 — КОМП. СХЕМ.'
CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_FULLWEEK = 'понедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n11:40-13:00 — ООП\n13:05-14:25 — ООП\n\nпятница\n10:00-11:20 — КОМП. СХЕМ.\n13:05-14:25 — КОМП. СХЕМ.'
CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_FULLWEEK = 'понедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n13:05-14:25 — ООП\n\nпятница\n13:05-14:25 — ООП\n14:30-15:50 — ООП'
CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_FULLWEEK = 'понедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n13:05-14:25 — ООП\n\nпятница\n13:05-14:25 — ООП\n14:30-15:50 — ООП'
CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_FULLWEEK = 'понедельник\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n11:40-13:00 — ООП\n13:05-14:25 — ООП\n\nпятница\nПАР НЕТ'
CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_FULLWEEK = 'понедельник\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n11:40-13:00 — ООП\n13:05-14:25 — ООП\n\nпятница\nПАР НЕТ'
CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_FULLWEEK = 'понедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n13:05-14:25 — ООП\n\nпятница\n13:05-14:25 — ООП\n14:30-15:50 — ООП'
CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_FULLWEEK = 'понедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.\n\nвторник\nПАР НЕТ\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n13:05-14:25 — ООП\n\nпятница\n13:05-14:25 — ООП\n14:30-15:50 — ООП'

CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY = '08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.'
CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY = '08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.'
CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY = '08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.'
CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY = '08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.'
CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY = '08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.'
CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY = '08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.'
CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY = '08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.'
CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY = '08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.'

CS18_SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY = SCHEDULE_TUESDAY_DAYOFF
CS18_SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY = SCHEDULE_TUESDAY_DAYOFF
CS18_SCHEDULE_DARKWEEK_1GROUP_TUESDAY = SCHEDULE_TUESDAY_DAYOFF
CS18_SCHEDULE_DARKWEEK_2GROUP_TUESDAY = SCHEDULE_TUESDAY_DAYOFF

CS18_SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY = '11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.'
CS18_SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY = '11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.'
CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY = '11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.'
CS18_SCHEDULE_DARKWEEK_2GROUP_WEDNESDAY = '11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.'

CS18_SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY = '11:40-13:00 — ООП\n13:05-14:25 — ООП'
CS18_SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY = '13:05-14:25 — ООП'
CS18_SCHEDULE_DARKWEEK_1GROUP_THURSDAY = '11:40-13:00 — ООП\n13:05-14:25 — ООП'
CS18_SCHEDULE_DARKWEEK_2GROUP_THURSDAY = '13:05-14:25 — ООП'

CS18_SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY = '08:30-09:50 — КОМП. СХЕМ.\n10:00-11:20 — КОМП. СХЕМ.'
CS18_SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY = '10:00-11:20 — КОМП. СХЕМ.\n13:05-14:25 — КОМП. СХЕМ.'
CS18_SCHEDULE_DARKWEEK_1GROUP_FRIDAY = SCHEDULE_FRIDAY_DAYOFF
CS18_SCHEDULE_DARKWEEK_2GROUP_FRIDAY = '13:05-14:25 — ООП\n14:30-15:50 — ООП'

CS18_SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY = SCHEDULE_SATURDAY_DAYOFF
CS18_SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY = SCHEDULE_SATURDAY_DAYOFF
CS18_SCHEDULE_DARKWEEK_1GROUP_SATURDAY = SCHEDULE_SATURDAY_DAYOFF
CS18_SCHEDULE_DARKWEEK_2GROUP_SATURDAY = SCHEDULE_SATURDAY_DAYOFF

CS18_SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY = SCHEDULE_SUNDAY_DAYOFF
CS18_SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY = SCHEDULE_SUNDAY_DAYOFF
CS18_SCHEDULE_DARKWEEK_1GROUP_SUNDAY = SCHEDULE_SUNDAY_DAYOFF
CS18_SCHEDULE_DARKWEEK_2GROUP_SUNDAY = SCHEDULE_SUNDAY_DAYOFF

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

date_today = datetime.date.today()
date_week = date_today.isocalendar()[1]
date_weekday = date_today.weekday()

now = datetime.datetime.now()
delta = datetime.timedelta(days=1)

date_today_day = now.day
date_today_month = now.month
date_tomorrow_day = (now + delta).day
date_tomorrow_month = (now + delta).month
date_yesterday_day = (now - delta).day
date_yesterday_month = (now - delta).month

if date_weekday == 0:
	date_monday_day = date_today.day
	date_monday_month = date_today.month
else:
	date_monday_day = (date_today + relativedelta(days=+1, weekday=MO(+1))).day
	date_monday_month = (date_today + relativedelta(days=+1, weekday=MO(+1))).month
if date_weekday == 1:
	date_tuesday_day = date_today.day
	date_tuesday_month = date_today.month
else:
	date_tuesday_day = (date_today + relativedelta(days=+1, weekday=TU(+1))).day
	date_tuesday_month = (date_today + relativedelta(days=+1, weekday=TU(+1))).month
if date_weekday == 2:
	date_wednesday_day = date_today.day
	date_wednesday_month = date_today.month
else:
	date_wednesday_day = (date_today + relativedelta(days=+1, weekday=WE(+1))).day
	date_wednesday_month = (date_today + relativedelta(days=+1, weekday=WE(+1))).month
if date_weekday == 3:
	date_thursday_day = date_today.day
	date_thursday_month = date_today.month
else:
	date_thursday_day = (date_today + relativedelta(days=+1, weekday=TH(+1))).day
	date_thursday_month = (date_today + relativedelta(days=+1, weekday=TH(+1))).month
if date_weekday == 4:
	date_friday_day = date_today.day
	date_friday_month = date_today.month
else:
	date_friday_day = (date_today + relativedelta(days=+1, weekday=FR(+1))).day
	date_friday_month = (date_today + relativedelta(days=+1, weekday=FR(+1))).month
if date_weekday == 5:
	date_saturday_day = date_today.day
	date_saturday_month = date_today.month
else:
	date_saturday_day = (date_today + relativedelta(days=+1, weekday=SA(+1))).day
	date_saturday_month = (date_today + relativedelta(days=+1, weekday=SA(+1))).month
if date_weekday == 6:
	date_sunday_day = date_today.day
	date_sunday_month = date_today.month
else:
	date_sunday_day = (date_today + relativedelta(days=+1, weekday=SU(+1))).day
	date_sunday_month = (date_today + relativedelta(days=+1, weekday=SU(+1))).month


date_today_format = '%02d' % date_today_day + '.' + '%02d' % date_today_month
date_tomorrow_format = '%02d' % date_tomorrow_day + '.' + '%02d' % date_tomorrow_month
date_yesterday_format = '%02d' % date_yesterday_day + '.' + '%02d' % date_yesterday_month

date_monday_format = '%02d' % date_monday_day + '.' + '%02d' % date_monday_month
date_tuesday_format = '%02d' % date_tuesday_day + '.' + '%02d' % date_tuesday_month
date_wednesday_format = '%02d' % date_wednesday_day + '.' + '%02d' % date_wednesday_month
date_thursday_format = '%02d' % date_thursday_day + '.' + '%02d' % date_thursday_month
date_friday_format = '%02d' % date_friday_day + '.' + '%02d' % date_friday_month
date_saturday_format = '%02d' % date_saturday_day + '.' + '%02d' % date_saturday_month
date_sunday_format = '%02d' % date_sunday_day + '.' + '%02d' % date_sunday_month

time_now = now.time()
time_day_beg = datetime.time(0, 0, 0)
time_uni_end = datetime.time(15, 50, 0)
time_day_end = datetime.time(23, 59, 59)

if (date_week % 2) == 0:
	weekorder = True
	week = 'светлая'
else:
	weekorder = False
	week = 'тёмная'

if date_weekday == 0:
	today = 'понедельник'
	today_list = ['понедельник', 'пн']
	tomorrow = 'вторник'
	tomorrow_list = ['вторник', 'вт']
	yesterday = 'воскресенье'
	yesterday_list = ['воскресенье', 'вс']
elif date_weekday == 1:
	today = 'вторник'
	today_list = ['вторник', 'вт']
	tomorrow = 'среда'
	tomorrow_list = ['среда', 'ср', 'среду']
	yesterday = 'понедельник'
	yesterday_list = ['понедельник', 'пн']
elif date_weekday == 2:
	today = 'среда'
	today_list = ['среда', 'ср', 'среду']
	tomorrow = 'четверг'
	tomorrow_list = ['четверг', 'чт']
	yesterday = 'вторник'
	yesterday_list = ['вторник', 'вт']
elif date_weekday == 3:
	today = 'четверг'
	today_list = ['четверг', 'чт']
	tomorrow = 'пятница'
	tomorrow_list = ['пятница', 'пт', 'пятницу']
	yesterday = 'среда'
	yesterday_list = ['среда', 'ср', 'среду']
elif date_weekday == 4:
	today = 'пятница'
	today_list = ['пятница', 'пт', 'пятницу']
	tomorrow = 'суббота'
	tomorrow_list = ['суббота', 'сб', 'субботу']
	yesterday = 'четверг'
	yesterday_list = ['четверг', 'чт']
elif date_weekday == 5:
	today = 'суббота'
	today_list = ['суббота', 'сб', 'субботу']
	tomorrow = 'воскресенье'
	tomorrow_list = ['воскресенье', 'вс']
	yesterday = 'пятница'
	yesterday_list = ['пятница', 'пт', 'пятницу']
elif date_weekday == 6:
	today = 'воскресенье'
	today_list = ['воскресенье', 'вс']
	tomorrow = 'понедельник'
	tomorrow_list = ['понедельник', 'пн']
	yesterday = 'суббота'
	yesterday_list = ['суббота', 'сб', 'субботу']

week_template = '\n' + week + ' неделя'

today_tag = today + ' / ' + date_today_format
tomorrow_tag = tomorrow + ' / ' + date_tomorrow_format
yesterday_tag = yesterday + ' / ' + date_yesterday_format
monday_tag = 'понедельник / ' + date_monday_format
tuesday_tag = 'вторник / ' + date_tuesday_format
wednesday_tag = 'среда / ' + date_wednesday_format
thursday_tag = 'четверг / ' + date_thursday_format
friday_tag = 'пятница / ' + date_friday_format
saturday_tag = 'суббота / ' + date_saturday_format
sunday_tag = 'воскресенье / ' + date_sunday_format

classes_list = ['пары', 'парам', 'расписание', 'расписанию', 'предметы', 'предметам']
day_list = ['какой день', 'какой сейчас день', 'какой сегодня день']
week_list = ['какая неделя', 'какая сейчас неделя', 'какая сегодня неделя']
days_list = ['сегодня', 'вчера', 'завтра']
weekdays_list = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье', 'среду', 'пятницу', 'субботу', 'пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
fullweek_list = ['неделя', 'неделе', 'неделю']
cancel_list = ['назад', 'отмена', 'выйти', 'выход']
exceptions_list = ['поза', 'после']
commands_list = ['schedule', 'classes']

@bot.message_handler(commands=['start'])
def start_message(message):
	cid = message.chat.id
	uid = message.from_user.id
	mct = message.chat.type

	if uid in first_group.keys():
		student_name = ', ' + first_group[uid].split(' ', 1)[0]
	elif uid in second_group.keys():
		student_name = ', ' + second_group[uid].split(' ', 1)[0]
	else:
		student_name = ''

	if mct == 'private':
		if uid in first_group.keys() or uid in second_group.keys():
			bot.send_message(cid, 'привет' + student_name + '!' + '\n\nиспользуй комманду /classes, что бы получить расписание\n\nсоздатель — @yoqwx')

@bot.message_handler(commands=['classes'])
def classes_command(message):
	cid = message.chat.id
	uid = message.from_user.id
	mct = message.chat.type

	if uid in first_group.keys():
		student_name = ', ' + first_group[uid].split(' ', 1)[0]
	elif uid in second_group.keys():
		student_name = ', ' + second_group[uid].split(' ', 1)[0]
	else:
		student_name = ''

	board_add = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
	board_add.row(types.KeyboardButton('вчера'), types.KeyboardButton('сегодня'), types.KeyboardButton('завтра'))
	board_add.row(types.KeyboardButton('пн'), types.KeyboardButton('вт'), types.KeyboardButton('ср'), types.KeyboardButton('чт'), types.KeyboardButton('пт'), types.KeyboardButton('сб'), types.KeyboardButton('вс'))
	board_add.row(types.KeyboardButton('вся неделя'), types.KeyboardButton('назад'))

	if mct == 'private':
		if uid in first_group.keys() or uid in second_group.keys():
			board_options = bot.reply_to(message, 'выбери день', reply_markup=board_add)
			bot.register_next_step_handler(board_options, predefined_messages)

def predefined_messages(message):
	msg = message.text.lower()
	mid = message.message_id
	cid = message.chat.id
	uid = message.from_user.id
	mct = message.chat.type
	
	if uid in first_group.keys():
		student_group = 'первая группа'
		student_name = first_group[uid].split(' ', 1)[0] + ', '
	elif uid in second_group.keys():
		student_group = 'вторая группа'
		student_name = second_group[uid].split(' ', 1)[0] + ', '
	else:
		student_group = ''
		student_name = ''

	student_def = student_name + student_group
	today_template = student_def + '\n(' + today_tag + ')'
	yesterday_template = student_def + '\n(' + yesterday_tag + ')'
	tomorrow_template = student_def + '\n(' + tomorrow_tag + ')'
	monday_template = student_def + '\n(' + monday_tag + ')'
	tuesday_template = student_def + '\n(' + tuesday_tag + ')'
	wednesday_template = student_def + '\n(' + wednesday_tag + ')'
	thursday_template = student_def + '\n(' + thursday_tag + ')'
	friday_template = student_def + '\n(' + friday_tag + ')'
	saturday_template = student_def + '\n(' + saturday_tag + ')'
	sunday_template = student_def + '\n(' + sunday_tag + ')'

	days_matches = sum(x in msg for x in days_list)
	weekdays_matches = sum(x in msg for x in weekdays_list)

	today_unnecessary_list = [word for word in today_list if word not in weekdays_list]
	yesterday_unnecessary_list = [word for word in yesterday_list if word not in weekdays_list]

	days_condition = 'ok'
	week_condition = 'ok'
	full_condition = 'ok'

	board_hide = types.ReplyKeyboardRemove()

	if 0 < days_matches < 2 and not any(word in msg for word in cancel_list) and not any(word in msg for word in exceptions_list):
		if 'сегодня' in msg:
			if not any(word in msg for word in weekdays_list):
				days_condition = 'ok'
			elif any(word in msg for word in today_list) and not any(word in msg for word in today_unnecessary_list):
				days_condition = 'ok'
			else:
				days_condition = 'not ok'
		elif 'завтра' in msg:
			if 0 < weekdays_matches < 2 and msg.count('вт') == 1:
				days_condition = 'ok'
			elif date_weekday == 0 and ('вторник' in msg or msg.count('вт') > 1) and not ('понедельник' in msg or 'среда' in msg or 'четверг' in msg or 'пятница' in msg or 'суббота' in msg or 'воскресенье' in msg or 'среду' in msg or 'пятницу' in msg or 'субботу' in msg or 'пн' in msg or 'ср' in msg or 'чт' in msg or 'пт' in msg or 'сб' in msg or 'вс' in msg):
				days_condition = 'ok'
			elif date_weekday == 1 and ('среда' in msg or 'ср' in msg or 'среду' in msg) and not ('понедельник' in msg or 'вторник' in msg or 'четверг' in msg or 'пятница' in msg or 'суббота' in msg or 'воскресенье' in msg or 'пятницу' in msg or 'субботу' in msg or 'пн' in msg or msg.count('вт') > 1 or 'чт' in msg or 'пт' in msg or 'сб' in msg or 'вс' in msg):
				days_condition = 'ok'
			elif date_weekday == 2 and ('четверг' in msg or 'чт' in msg) and not ('понедельник' in msg or 'вторник' in msg or 'среда' in msg or 'пятница' in msg or 'суббота' in msg or 'воскресенье' in msg or 'среду' in msg or 'пятницу' in msg or 'субботу' in msg or 'пн' in msg or msg.count('вт') > 1 or 'ср' in msg or 'пт' in msg or 'сб' in msg or 'вс' in msg):
				days_condition = 'ok'
			elif date_weekday == 3 and ('пятница' in msg or 'пт' in msg or 'пятницу' in msg) and not ('понедельник' in msg or 'вторник' in msg or 'среда' in msg or 'четверг' in msg or 'суббота' in msg or 'воскресенье' in msg or 'среду' in msg or 'субботу' in msg or 'пн' in msg or msg.count('вт') > 1 or 'ср' in msg or 'чт' in msg or 'сб' in msg or 'вс' in msg):
				days_condition = 'ok'
			elif date_weekday == 4 and ('суббота' in msg or 'сб' in msg or 'субботу' in msg) and not ('понедельник' in msg or 'вторник' in msg or 'среда' in msg or 'четверг' in msg or 'пятница' in msg or 'воскресенье' in msg or 'среду' in msg or 'пятницу' in msg or 'пн' in msg or msg.count('вт') > 1 or 'ср' in msg or 'чт' in msg or 'пт' in msg or 'вс' in msg):
				days_condition = 'ok'
			elif date_weekday == 5 and ('воскресенье' in msg or 'вс' in msg) and not ('понедельник' in msg or 'вторник' in msg or 'среда' in msg or 'четверг' in msg or 'пятница' in msg or 'суббота' in msg or 'среду' in msg or 'пятницу' in msg or 'субботу' in msg or 'пн' in msg or msg.count('вт') > 1 or 'ср' in msg or 'чт' in msg or 'пт' in msg or 'сб' in msg):
				days_condition = 'ok'
			elif date_weekday == 6 and ('понедельник' in msg or 'пн' in msg) and not ('вторник' in msg or 'среда' in msg or 'четверг' in msg or 'пятница' in msg or 'суббота' in msg or 'воскресенье' in msg or 'среду' in msg or 'пятницу' in msg or 'субботу' in msg or msg.count('вт') > 1 or 'ср' in msg or 'чт' in msg or 'пт' in msg or 'сб' in msg or 'вс' in msg):
				days_condition = 'ok'
			else:
				days_condition = 'not ok'
		elif 'вчера' in msg:
			if not any(word in msg for word in weekdays_list):
				days_condition = 'ok'
			elif any(word in msg for word in yesterday_list) and not any(word in msg for word in yesterday_unnecessary_list):
				days_condition = 'ok'
			else:
				days_condition = 'not ok'
	else:
		days_condition = 'not ok'

	if not any(word in msg for word in days_list) and not any(word in msg for word in cancel_list) and not any(word in msg for word in exceptions_list):
		if ('понедельник' in msg or 'пн' in msg) and not ('вторник' in msg or 'среда' in msg or 'четверг' in msg or 'пятница' in msg or 'суббота' in msg or 'воскресенье' in msg or 'среду' in msg or 'пятницу' in msg or 'субботу' in msg or 'вт' in msg or 'ср' in msg or 'чт' in msg or 'пт' in msg or 'сб' in msg or 'вс' in msg):
			week_condition = 'ok'
		elif ('вторник' in msg or 'вт' in msg) and not ('понедельник' in msg or 'среда' in msg or 'четверг' in msg or 'пятница' in msg or 'суббота' in msg or 'воскресенье' in msg or 'среду' in msg or 'пятницу' in msg or 'субботу' in msg or 'пн' in msg or 'ср' in msg or 'чт' in msg or 'пт' in msg or 'сб' in msg or 'вс' in msg):
			week_condition = 'ok'
		elif ('среда' in msg or 'ср' in msg or 'среду' in msg) and not ('понедельник' in msg or 'вторник' in msg or 'четверг' in msg or 'пятница' in msg or 'суббота' in msg or 'воскресенье' in msg or 'пятницу' in msg or 'субботу' in msg or 'пн' in msg or 'вт' in msg or 'чт' in msg or 'пт' in msg or 'сб' in msg or 'вс' in msg):
			week_condition = 'ok'
		elif ('четверг' in msg or 'чт' in msg) and not ('понедельник' in msg or 'вторник' in msg or 'среда' in msg or 'пятница' in msg or 'суббота' in msg or 'воскресенье' in msg or 'среду' in msg or 'пятницу' in msg or 'субботу' in msg or 'пн' in msg or 'вт' in msg or 'ср' in msg or 'пт' in msg or 'сб' in msg or 'вс' in msg):
			week_condition = 'ok'
		elif ('пятница' in msg or 'пт' in msg or 'пятницу' in msg) and not ('понедельник' in msg or 'вторник' in msg or 'среда' in msg or 'четверг' in msg or 'суббота' in msg or 'воскресенье' in msg or 'среду' in msg or 'субботу' in msg or 'пн' in msg or 'вт' in msg or 'ср' in msg or 'чт' in msg or 'сб' in msg or 'вс' in msg):
			week_condition = 'ok'
		elif ('суббота' in msg or 'сб' in msg or 'субботу' in msg) and not ('понедельник' in msg or 'вторник' in msg or 'среда' in msg or 'четверг' in msg or 'пятница' in msg or 'воскресенье' in msg or 'среду' in msg or 'пятницу' in msg or 'пн' in msg or 'вт' in msg or 'ср' in msg or 'чт' in msg or 'пт' in msg or 'вс' in msg):
			week_condition = 'ok'
		elif ('воскресенье' in msg or 'вс' in msg) and not ('понедельник' in msg or 'вторник' in msg or 'среда' in msg or 'четверг' in msg or 'пятница' in msg or 'суббота' in msg or 'среду' in msg or 'пятницу' in msg or 'субботу' in msg or 'пн' in msg or 'вт' in msg or 'ср' in msg or 'чт' in msg or 'пт' in msg or 'сб' in msg):
			if 'вся' not in msg and 'всю' not in msg:
				week_condition = 'ok'
			else:
				week_condition = 'not ok'
		else:
			week_condition = 'not ok'
	else:
		week_condition = 'not ok'

	if any(word in msg for word in fullweek_list) and not any(word in msg for word in days_list) and not any(word in msg for word in cancel_list) and not any(word in msg for word in exceptions_list):
		if not any(word in msg for word in weekdays_list):
			full_condition = 'ok'
		elif ('вся' in msg or 'всю' in msg) and 0 < weekdays_matches < 2:
			full_condition = 'ok'
		else:
			full_condition = 'not ok'
	else:
		full_condition = 'not ok'

	if any(word in msg for word in cancel_list) and not any(word in msg for word in days_list) and not any(word in msg for word in weekdays_list) and not any(word in msg for word in fullweek_list) and not any(word in msg for word in exceptions_list):
		cancel_condition = 'ok'
	else:
		cancel_condition = 'not ok'

	if weekorder == True:
		if uid in first_group.keys():
			if days_condition == 'ok':
				if 'вчера' in msg:
					if date_weekday == 0:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 1:
						if uid in first_group_eng.keys():
							bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
						elif uid in second_group_eng.keys():
							bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 2:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 3:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 4:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 5:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 6:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'сегодня' in msg:
					if date_weekday == 0:
						if uid in first_group_eng.keys():
							bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
						elif uid in second_group_eng.keys():
							bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 1:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 2:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 3:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 4:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 5:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 6:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'завтра' in msg:
					if date_weekday == 0:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 1:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 2:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 3:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 4:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 5:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 6:
						if uid in first_group_eng.keys():
							bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
						elif uid in second_group_eng.keys():
							bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
			elif week_condition == 'ok':
				if 'понедельник' in msg or 'пн' in msg:
					if uid in first_group_eng.keys():
						bot.send_message(cid, monday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif uid in second_group_eng.keys():
						bot.send_message(cid, monday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'вторник' in msg or 'вт' in msg:
					if uid in first_group.keys():
						bot.send_message(cid, tuesday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_TUESDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'среда' in msg or 'ср' in msg or 'среду' in msg:
						bot.send_message(cid, wednesday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'четверг' in msg or 'чт' in msg:
						bot.send_message(cid, thursday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_THURSDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'пятница' in msg or 'пт' in msg or 'пятницу' in msg:
						bot.send_message(cid, friday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_FRIDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'суббота' in msg or 'сб' in msg or 'субботу' in msg:
						bot.send_message(cid, saturday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SATURDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'воскресенье' in msg or 'вс' in msg:
						bot.send_message(cid, sunday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_SUNDAY, reply_to_message_id=mid, reply_markup=board_hide)
			elif full_condition == 'ok':
				bot.send_message(cid, student_group + week_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_1GROUP_1SUBGROUP_FULLWEEK, reply_markup=board_hide)
			elif cancel_condition == 'ok':
				bot.send_message(cid, 'хорошо', reply_to_message_id=mid, reply_markup=board_hide)
				time.sleep(3)
				bot.delete_message(cid, mid)
				bot.delete_message(cid, mid - 1)
				bot.delete_message(cid, mid - 2)
			elif days_condition == 'not ok' or week_condition == 'not ok' or full_condition == 'not ok':
				error_msg = bot.send_message(cid, '?', reply_to_message_id=mid)
				bot.register_next_step_handler(error_msg, predefined_messages)
		elif uid in second_group.keys():
			if days_condition == 'ok':
				if 'вчера' in msg:
					if date_weekday == 0:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 1:
						if uid in first_group_eng.keys():
							bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
						elif uid in second_group_eng.keys():
							bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 2:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 3:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 4:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 5:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 6:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'сегодня' in msg:
					if date_weekday == 0:
						if uid in first_group_eng.keys():
							bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
						elif uid in second_group_eng.keys():
							bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 1:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 2:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 3:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 4:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 5:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 6:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'завтра' in msg:
					if date_weekday == 0:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 1:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 2:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 3:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 4:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 5:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 6:
						if uid in first_group_eng.keys():
							bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
						elif uid in second_group_eng.keys():
							bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
			elif week_condition == 'ok':
				if 'понедельник' in msg or 'пн' in msg:
					if uid in first_group_eng.keys():
						bot.send_message(cid, monday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif uid in second_group_eng.keys():
						bot.send_message(cid, monday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'вторник' in msg or 'вт' in msg:
					if uid in first_group.keys():
						bot.send_message(cid, tuesday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_TUESDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'среда' in msg or 'ср' in msg or 'среду' in msg:
						bot.send_message(cid, wednesday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'четверг' in msg or 'чт' in msg:
						bot.send_message(cid, thursday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_THURSDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'пятница' in msg or 'пт' in msg or 'пятницу' in msg:
						bot.send_message(cid, friday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_FRIDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'суббота' in msg or 'сб' in msg or 'субботу' in msg:
						bot.send_message(cid, saturday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SATURDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'воскресенье' in msg or 'вс' in msg:
						bot.send_message(cid, sunday_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_SUNDAY, reply_to_message_id=mid, reply_markup=board_hide)
			elif full_condition == 'ok':
				bot.send_message(cid, student_group + week_template + '\n\n' + CS18_SCHEDULE_LIGHTWEEK_2GROUP_1SUBGROUP_FULLWEEK, reply_markup=board_hide)
			elif cancel_condition == 'ok':
				bot.send_message(cid, 'хорошо', reply_to_message_id=mid, reply_markup=board_hide)
				time.sleep(3)
				bot.delete_message(cid, mid)
				bot.delete_message(cid, mid - 1)
				bot.delete_message(cid, mid - 2)
			elif days_condition == 'not ok' or week_condition == 'not ok' or full_condition == 'not ok':
				error_msg = bot.send_message(cid, '?', reply_to_message_id=mid)
				bot.register_next_step_handler(error_msg, predefined_messages)
	elif weekorder == False:
		if uid in first_group.keys():
			if days_condition == 'ok':
				if 'вчера' in msg:
					if date_weekday == 0:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_SUNDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 1:
						if uid in first_group_eng.keys():
							bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
						elif uid in second_group_eng.keys():
							bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 2:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 3:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 4:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 5:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 6:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_SATURDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'сегодня' in msg:
					if date_weekday == 0:
						if uid in first_group_eng.keys():
							bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
						elif uid in second_group_eng.keys():
							bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 1:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 2:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 3:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 4:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 5:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_SATURDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 6:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_SUNDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'завтра' in msg:
					if date_weekday == 0:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 1:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 2:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 3:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 4:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_SATURDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 5:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_SUNDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 6:
						if uid in first_group_eng.keys():
							bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
						elif uid in second_group_eng.keys():
							bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
			elif week_condition == 'ok':
				if 'понедельник' in msg or 'пн' in msg:
					if uid in first_group_eng.keys():
						bot.send_message(cid, monday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif uid in second_group_eng.keys():
						bot.send_message(cid, monday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'вторник' in msg or 'вт' in msg:
					if uid in first_group.keys():
						bot.send_message(cid, tuesday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_TUESDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'среда' in msg or 'ср' in msg or 'среду' in msg:
						bot.send_message(cid, wednesday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_WEDNESDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'четверг' in msg or 'чт' in msg:
						bot.send_message(cid, thursday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_THURSDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'пятница' in msg or 'пт' in msg or 'пятницу' in msg:
						bot.send_message(cid, friday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_FRIDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'суббота' in msg or 'сб' in msg or 'субботу' in msg:
						bot.send_message(cid, saturday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_SATURDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'воскресенье' in msg or 'вс' in msg:
						bot.send_message(cid, sunday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_SUNDAY, reply_to_message_id=mid, reply_markup=board_hide)
			elif full_condition == 'ok':
				bot.send_message(cid, student_group + week_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_1GROUP_1SUBGROUP_FULLWEEK, reply_markup=board_hide)
			elif cancel_condition == 'ok':
				bot.send_message(cid, 'хорошо', reply_to_message_id=mid, reply_markup=board_hide)
				time.sleep(3)
				bot.delete_message(cid, mid)
				bot.delete_message(cid, mid - 1)
				bot.delete_message(cid, mid - 2)
			elif days_condition == 'not ok' or week_condition == 'not ok' or full_condition == 'not ok':
				error_msg = bot.send_message(cid, '?', reply_to_message_id=mid)
				bot.register_next_step_handler(error_msg, predefined_messages)
		elif uid in second_group.keys():
			if days_condition == 'ok':
				if 'вчера' in msg:
					if date_weekday == 0:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_SUNDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 1:
						if uid in first_group_eng.keys():
							bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
						elif uid in second_group_eng.keys():
							bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 2:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 3:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 4:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 5:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 6:
						bot.send_message(cid, yesterday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_SATURDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'сегодня' in msg:
					if date_weekday == 0:
						if uid in first_group_eng.keys():
							bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
						elif uid in second_group_eng.keys():
							bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 1:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 2:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 3:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 4:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 5:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_SATURDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 6:
						bot.send_message(cid, today_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_SUNDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'завтра' in msg:
					if date_weekday == 0:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 1:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 2:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 3:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 4:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_SATURDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 5:
						bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_SUNDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif date_weekday == 6:
						if uid in first_group_eng.keys():
							bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
						elif uid in second_group_eng.keys():
							bot.send_message(cid, tomorrow_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
			elif week_condition == 'ok':
				if 'понедельник' in msg or 'пн' in msg:
					if uid in first_group_eng.keys():
						bot.send_message(cid, monday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
					elif uid in second_group_eng.keys():
						bot.send_message(cid, monday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_2SUBGROUP_MONDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'вторник' in msg or 'вт' in msg:
					if uid in first_group.keys():
						bot.send_message(cid, tuesday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_TUESDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'среда' in msg or 'ср' in msg or 'среду' in msg:
						bot.send_message(cid, wednesday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_WEDNESDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'четверг' in msg or 'чт' in msg:
						bot.send_message(cid, thursday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_THURSDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'пятница' in msg or 'пт' in msg or 'пятницу' in msg:
						bot.send_message(cid, friday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_FRIDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'суббота' in msg or 'сб' in msg or 'субботу' in msg:
						bot.send_message(cid, saturday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_SATURDAY, reply_to_message_id=mid, reply_markup=board_hide)
				elif 'воскресенье' in msg or 'вс' in msg:
						bot.send_message(cid, sunday_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_SUNDAY, reply_to_message_id=mid, reply_markup=board_hide)
			elif full_condition == 'ok':
				bot.send_message(cid, student_group + week_template + '\n\n' + CS18_SCHEDULE_DARKWEEK_2GROUP_1SUBGROUP_FULLWEEK, reply_markup=board_hide)
			elif cancel_condition == 'ok':
				bot.send_message(cid, 'хорошо', reply_to_message_id=mid, reply_markup=board_hide)
				time.sleep(3)
				bot.delete_message(cid, mid)
				bot.delete_message(cid, mid - 1)
				bot.delete_message(cid, mid - 2)
			elif days_condition == 'not ok' or week_condition == 'not ok' or full_condition == 'not ok':
				error_msg = bot.send_message(cid, '?', reply_to_message_id=mid)
				bot.register_next_step_handler(error_msg, predefined_messages)

@bot.message_handler(content_types=['sticker'])
def predefined_stickers(message):
	cid = message.chat.id
	uid = message.from_user.id
	mct = message.chat.type

	sticker_rnm = random.randint(1, 25)

	if sticker_rnm == 1:
		sid = 'CAADAgADNwADTV8oGAcnDK_zzifQFgQ'
	elif sticker_rnm == 2:
		sid = 'CAADAgADOAADTV8oGIkHWmw4--6sFgQ'
	elif sticker_rnm == 3:
		sid = 'CAADAgADOQADTV8oGB0jpTwBtJ3qFgQ'
	elif sticker_rnm == 4:
		sid = 'CAADAgADOgADTV8oGMRKEjeYMD-iFgQ'
	elif sticker_rnm == 5:
		sid = 'CAADAgADOwADTV8oGPYpjAugj5MkFgQ'
	elif sticker_rnm == 6:
		sid = 'CAADAgADPAADTV8oGNHRaGn8VRqSFgQ'
	elif sticker_rnm == 7:
		sid = 'CAADAgADPQADTV8oGGv7CE-jUh8EFgQ'
	elif sticker_rnm == 8:
		sid = 'CAADAgADPwADTV8oGGEa15DV51VsFgQ'
	elif sticker_rnm == 9:
		sid = 'CAADAgADQQADTV8oGHxIB3e9wuKQFgQ'
	elif sticker_rnm == 10:
		sid = 'CAADAgADQgADTV8oGOKRYZfYhYJFFgQ'
	elif sticker_rnm == 11:
		sid = 'CAADAgADQwADTV8oGE78wiPH81acFgQ'
	elif sticker_rnm == 12:
		sid = 'CAADAgADRAADTV8oGAtV7hSpVNtaFgQ'
	elif sticker_rnm == 13:
		sid = 'CAADAgADRQADTV8oGFslQVK175XIFgQ'
	elif sticker_rnm == 14:
		sid = 'CAADAgADRgADTV8oGNfQA4YP9hbGFgQ'
	elif sticker_rnm == 15:
		sid = 'CAADAgADRwADTV8oGE_kCZ6bNeYWFgQ'
	elif sticker_rnm == 16:
		sid = 'CAADAgADSAADTV8oGAW7JHvjQFXFFgQ'
	elif sticker_rnm == 17:
		sid = 'CAADAgADSQADTV8oGJ2B3Lds1bOCFgQ'
	elif sticker_rnm == 18:
		sid = 'CAADAgADSgADTV8oGM58vpLz3FuoFgQ'
	elif sticker_rnm == 19:
		sid = 'CAADAgADSwADTV8oGOxJeXJbuuKHFgQ'
	elif sticker_rnm == 20:
		sid = 'CAADAgADTQADTV8oGLiiZvA26ikuFgQ'
	elif sticker_rnm == 21:
		sid = 'CAADAgADTAADTV8oGJhTCjwdw5EYFgQ'
	elif sticker_rnm == 22:
		sid = 'CAADAgADTwADTV8oGJzFxvw-eMa5FgQ'
	elif sticker_rnm == 23:
		sid = 'CAADAgADTgADTV8oGOMvW5CjVqGhFgQ'
	elif sticker_rnm == 24:
		sid = 'CAADAgADUAADTV8oGMB0LsS6SDJtFgQ'
	elif sticker_rnm == 25:
		sid = 'CAADAgADUQADTV8oGM5oZrUGiKN-FgQ'

	if mct == 'private':
		if uid in first_group.keys() or uid in second_group.keys():
			bot.send_sticker(cid, sid)

@app.route('/'+ TOKEN, methods=['POST'])
def get_messages():
	bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode('utf-8'))])
	return '', 200

@app.route('/')
def process_webhook():
	bot.remove_webhook()
	time.sleep(1)
	bot.set_webhook(url='https://iiktbot.herokuapp.com/' + TOKEN)
	return '', 200

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 443)))

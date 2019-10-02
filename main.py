from datetime import date, timedelta
import telebot
from telebot import types

bot = telebot.TeleBot('642122532:AAGKg4s2_ffJqDNTrqvbI7-qeFRxNEOBPV8')

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, "привет, чем могу быть полезен?")

@bot.message_handler(content_types=['text'])
def predefined_commands(message):
	first_group = {('Виталий'):405299021, ('Юля'):393708492, ('Андрей'):416924459, ('Влад'):613759219, ('Женя'):548116631, ('Карина'):379537100, ('Денис'):635991556, ('Дима'):349737926, ('Дима'):451287655, ('Степан'):469338261, ('Денис'):542413243, ('Женя'):692445612, ('Полина'):123456789, ('Саша'):52960692}
	second_group = {('Илья'):358734682, ('Саша'):537784508, ('Богдан'):448401733, ('Влад'):643705130, ('Леша'):605903256, ('Олег'):384343953, ('Влад'):655298761, ('Дима'):384173347, ('Денис'):780853105}
	first_group_eng = {('Виталий'):405299021, ('Влад'):643705130, ('Андрей'):416924459, ('Денис'):542413243, ('Денис'):635991556, ('Дима'):349737926, ('Дима'):451287655, ('Женя'):692445612, ('Полина'):123456789, ('Саша'):52960692, ('Денис'):780853105, ('Дима'):384173347, ('Влад'):655298761}
	second_group_eng = {('Юля'):393708492, ('Карина'):379537100, ('Женя'):548116631, ('Влад'):613759219, ('Степан'):469338261, ('Олег'):384343953, ('Илья'):358734682, ('Саша'):537784508, ('Богдан'):448401733, ('Леша'):605903256}
	all_students = {**first_group,**second_group}
	weeknum = date.today().isocalendar()[1]
	message.text = message.text.lower()
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
	if "какая" in message.text and "неделя" in message.text:
		bot.send_message(message.chat.id, "сейчас " + week + " неделя", reply_to_message_id = message.message_id)
	for name, identifier in all_students.items():
		if identifier == message.from_user.id:
			student_name = name.lower()
	for name, identifier in first_group.items():
		if identifier == message.from_user.id:
			student_group = "первая"
	for name, identifier in second_group.items():
		if identifier == message.from_user.id:
			student_group = "вторая"
	if weekorder == True:
		if date.today().weekday() == 0 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня светлый " + today, reply_to_message_id = message.message_id)
		elif date.today().weekday() == 1 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня светлый " + today, reply_to_message_id = message.message_id)
		elif date.today().weekday() == 2 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня светлая " + today, reply_to_message_id = message.message_id)
		elif date.today().weekday() == 3 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня светлый " + today, reply_to_message_id = message.message_id)
		elif date.today().weekday() == 4 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня светлая " + today, reply_to_message_id = message.message_id)
		elif date.today().weekday() == 5 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня светлая " + today, reply_to_message_id = message.message_id)
		elif date.today().weekday() == 6 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня светлое " + today, reply_to_message_id = message.message_id)
		if "сегодня" in message.text and "вчера" not in message.text and "завтра" not in message.text:
			if "пары" in message.text or "на сколько" in message.text or "парам" in message.text or "расписание" in message.text or "расписанию" in message.text or "предметы" in message.text or "предметам" in message.text or "у нас завтра" in message.text and today not in message.text:
				if message.from_user.id in first_group.values():
					if date.today().weekday() == 0:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n11:40-13:00 — ООП\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n08:30-09:50 — КОМП. СХЕМ.\n10:00-11:20 — КОМП. СХЕМ.", reply_to_message_id = message.message_id)
				elif message.from_user.id in second_group.values():
					if date.today().weekday() == 0:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n10:00-11:20 — КОМП. СХЕМ.\n13:05-14:25 — КОМП. СХЕМ.", reply_to_message_id = message.message_id)
				elif message.from_user.id not in all_students.values():
					bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id = message.message_id)
		elif "завтра" in message.text and "вчера" not in message.text and "сегодня" not in message.text:
			if "пары" in message.text or "на сколько" in message.text or "парам" in message.text or "расписание" in message.text or "расписанию" in message.text or "предметы" in message.text or "предметам" in message.text or "у нас завтра" in message.text and today not in message.text:
				if message.from_user.id in first_group.values():
					if date.today().weekday() + 1 == 7:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n11:40-13:00 — ООП\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n08:30-09:50 — КОМП. СХЕМ.\n10:00-11:20 — КОМП. СХЕМ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 5:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 6:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\nвоскресенье, пар нет", reply_to_message_id = message.message_id)
				elif message.from_user.id in second_group.values():
					if date.today().weekday() + 1 == 7:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n10:00-11:20 — КОМП. СХЕМ.\n13:05-14:25 — КОМП. СХЕМ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 5:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 6:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\nвоскресенье, пар нет", reply_to_message_id = message.message_id)
				elif message.from_user.id not in all_students.values():
					bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id = message.message_id)
		elif "вчера" in message.text and "завтра" not in message.text and "сегодня" not in message.text:
			if "пары" in message.text or "на сколько" in message.text or "парам" in message.text or "расписание" in message.text or "расписанию" in message.text or "предметы" in message.text or "предметам" in message.text or "у нас завтра" in message.text and today not in message.text:
				if message.from_user.id in first_group.values():
					if date.today().weekday() - 1 == 0:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n11:40-13:00 — ООП\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n08:30-09:50 — КОМП. СХЕМ.\n10:00-11:20 — КОМП. СХЕМ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 5:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 6:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\nвоскресенье, пар нет", reply_to_message_id = message.message_id)
				elif message.from_user.id in second_group.values():
					if date.today().weekday() - 1 == 0:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n10:00-11:20 — КОМП. СХЕМ.\n13:05-14:25 — КОМП. СХЕМ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 5:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 6:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\nвоскресенье, пар нет", reply_to_message_id = message.message_id)
				elif message.from_user.id not in all_students.values():
					bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id = message.message_id)
		elif "сегодня" not in message.text and "вчера" not in message.text and "завтра" not in message.text:
			if "пары" in message.text or "на сколько" in message.text or "парам" in message.text or "расписание" in message.text or "расписанию" in message.text or "предметы" in message.text or "предметам" in message.text or "у нас завтра" in message.text and today not in message.text:
				if message.from_user.id in first_group.values():
					if date.today().weekday() == 0 and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 1  and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 2  and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 3  and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n11:40-13:00 — ООП\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 4  and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n08:30-09:50 — КОМП. СХЕМ.\n10:00-11:20 — КОМП. СХЕМ.", reply_to_message_id = message.message_id)
					elif "понедельник" in message.text or "пн" in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (понедельник)\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (понедельник)\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif "вторник" in message.text or "вт" in message.text and "понедельник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (вторник)\n\nпар нет", reply_to_message_id = message.message_id)
					elif "среда" in message.text or "среду" in message.text or "ср" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (среда)\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif "четверг" in message.text or "чт" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (четверг)\n\n11:40-13:00 — ООП\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif "пятница" in message.text or "пятницу" in message.text or "пт" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (пятница)\n\n08:30-09:50 — КОМП. СХЕМ.\n10:00-11:20 — КОМП. СХЕМ.", reply_to_message_id = message.message_id)
					elif "суббота" in message.text or "субботу" in message.text or "сб" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (суббота)\n\nпар нет", reply_to_message_id = message.message_id)
					elif "воскресенье" in message.text or "вс" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (воскресенье)\n\nвоскресенье, пар нет", reply_to_message_id = message.message_id)
				elif message.from_user.id in second_group.values():
					if date.today().weekday() == 0 and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 1 and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 2 and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 3 and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 4 and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n10:00-11:20 — КОМП. СХЕМ.\n13:05-14:25 — КОМП. СХЕМ.", reply_to_message_id = message.message_id)
					elif "понедельник" in message.text or "пн" in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (понедельник)\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (понедельник)\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif "вторник" in message.text or "вт" in message.text and "понедельник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (вторник)\n\nпар нет", reply_to_message_id = message.message_id)
					elif "среда" in message.text or "среду" in message.text or "ср" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (среда)\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif "четверг" in message.text or "чт" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (четверг)\n\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif "пятница" in message.text or "пятницу" in message.text or "пт" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (пятница)\n\n10:00-11:20 — КОМП. СХЕМ.\n13:05-14:25 — КОМП. СХЕМ.", reply_to_message_id = message.message_id)
					elif "суббота" in message.text or "субботу" in message.text or "сб" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (суббота)\n\nпар нет", reply_to_message_id = message.message_id)
					elif "воскресенье" in message.text or "вс" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (воскресенье)\n\nвоскресенье, пар нет", reply_to_message_id = message.message_id)
				elif message.from_user.id not in all_students.values():
					bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id = message.message_id)
		if "schedule" in message.text:
			if message.from_user.id in first_group.values():
				if message.from_user.id in first_group_eng.values():
					bot.send_message(message.chat.id, student_group + " группа" + " / " + week + " неделя" + "\n\nпонедельник\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.\n\nвторник\nпар нет\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n11:40-13:00 — ООП\n13:05-14:25 — ООП\n\nпятница\n08:30-09:50 — КОМП. СХЕМ.\n10:00-11:20 — КОМП. СХЕМ.")
				elif message.from_user.id in second_group_eng.values():
					bot.send_message(message.chat.id, student_group + " группа" + " / " + week + " неделя" + "\n\nпонедельник\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.\n\nвторник\nпар нет\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n11:40-13:00 — ООП\n13:05-14:25 — ООП\n\nпятница\n10:00-11:20 — КОМП. СХЕМ.\n13:05-14:25 — КОМП. СХЕМ.")
			elif message.from_user.id in second_group.values():
				if message.from_user.id in first_group_eng.values():
					bot.send_message(message.chat.id, student_group + " группа" + " / " + week + " неделя" + "\n\nпонедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.\n\nвторник\nпар нет\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n13:05-14:25 — ООП\n\nпятница\n13:05-14:25 — ООП\n14:30-15:50 — ООП")
				elif message.from_user.id in second_group_eng.values():
					bot.send_message(message.chat.id, student_group + " группа" + " / " + week + " неделя" + "\n\nпонедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.\n\nвторник\nпар нет\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n13:05-14:25 — ООП\n\nпятница\n13:05-14:25 — ООП\n14:30-15:50 — ООП")
			elif message.from_user.id not in all_students.values():
				bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id = message.message_id)
	elif weekorder == False:
		if date.today().weekday() == 0 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня тёмный " + today, reply_to_message_id = message.message_id)
		elif date.today().weekday() == 1 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня тёмный " + today, reply_to_message_id = message.message_id)
		elif date.today().weekday() == 2 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня тёмная " + today, reply_to_message_id = message.message_id)
		elif date.today().weekday() == 3 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня тёмный " + today, reply_to_message_id = message.message_id)
		elif date.today().weekday() == 4 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня тёмная " + today, reply_to_message_id = message.message_id)
		elif date.today().weekday() == 5 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня тёмная " + today, reply_to_message_id = message.message_id)
		elif date.today().weekday() == 6 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня тёмное " + today, reply_to_message_id = message.message_id)
		if "сегодня" in message.text and "вчера" not in message.text and "завтра" not in message.text:
			if "пары" in message.text or "на сколько" in message.text or "парам" in message.text or "расписание" in message.text or "расписанию" in message.text or "предметы" in message.text or "предметам" in message.text or "у нас завтра" in message.text:
				if message.from_user.id in first_group.values():
					if date.today().weekday() == 0:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n11:40-13:00 — ООП\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\nпар нет", reply_to_message_id = message.message_id)
				elif message.from_user.id in second_group.values():
					if date.today().weekday() == 0:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n13:05-14:25 — ООП\n14:30-15:50 — ООП", reply_to_message_id = message.message_id)
				elif message.from_user.id not in all_students.values():
					bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id = message.message_id)
		elif "завтра" in message.text and "вчера" not in message.text and "сегодня" not in message.text:
			if "пары" in message.text or "на сколько" in message.text or "парам" in message.text or "расписание" in message.text or "расписанию" in message.text or "предметы" in message.text or "предметам" in message.text or "у нас завтра" in message.text:
				if message.from_user.id in first_group.values():
					if date.today().weekday() + 1 == 7:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n11:40-13:00 — ООП\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 5:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 6:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\nвоскресенье, пар нет", reply_to_message_id = message.message_id)
				elif message.from_user.id in second_group.values():
					if date.today().weekday() + 1 == 7:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\n13:05-14:25 — ООП\n14:30-15:50 — ООП", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 5:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 6:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + tomorrow + ")" + "\n\nвоскресенье, пар нет", reply_to_message_id = message.message_id)
				elif message.from_user.id not in all_students.values():
					bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id = message.message_id)
		elif "вчера" in message.text and "завтра" not in message.text and "сегодня" not in message.text:
			if "пары" in message.text or "на сколько" in message.text or "парам" in message.text or "расписание" in message.text or "расписанию" in message.text or "предметы" in message.text or "предметам" in message.text or "у нас завтра" in message.text:
				if message.from_user.id in first_group.values():
					if date.today().weekday() - 1 == 0:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n11:40-13:00 — ООП\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 5:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 6:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\nвоскресенье, пар нет", reply_to_message_id = message.message_id)
				elif message.from_user.id in second_group.values():
					if date.today().weekday() - 1 == 0:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\n13:05-14:25 — ООП\n14:30-15:50 — ООП", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 5:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() - 1 == 6:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + yesterday + ")" + "\n\nвоскресенье, пар нет", reply_to_message_id = message.message_id)
				elif message.from_user.id not in all_students.values():
					bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id = message.message_id)
		elif "сегодня" not in message.text and "вчера" not in message.text and "завтра" not in message.text:
			if "пары" in message.text or "на сколько" in message.text or "парам" in message.text or "расписание" in message.text or "расписанию" in message.text or "предметы" in message.text or "предметам" in message.text or "у нас завтра" in message.text:
				if message.from_user.id in first_group.values():
					if date.today().weekday() == 0 and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 1 and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 2 and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 3 and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n11:40-13:00 — ООП\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 4 and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\nпар нет", reply_to_message_id = message.message_id)
					elif "понедельник" in message.text or "пн" in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (понедельник)\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (понедельник)\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif "вторник" in message.text or "вт" in message.text and "понедельник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (вторник)\n\nпар нет", reply_to_message_id = message.message_id)
					elif "среда" in message.text or "среду" in message.text or "ср" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (среда)\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif "четверг" in message.text or "чт" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (четверг)\n\n11:40-13:00 — ООП\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif "пятница" in message.text or "пятницу" in message.text or "пт" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (пятница)\n\nпар нет", reply_to_message_id = message.message_id)
					elif "суббота" in message.text or "субботу" in message.text or "сб" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (суббота)\n\nпар нет", reply_to_message_id = message.message_id)
					elif "воскресенье" in message.text or "вс" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (воскресенье)\n\nвоскресенье, пар нет", reply_to_message_id = message.message_id)
				elif message.from_user.id in second_group.values():
					if date.today().weekday() == 0 and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 1 and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\nпар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 2 and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 3 and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 4 and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text and "пн" not in message.text and "вт" not in message.text and "ср" not in message.text and "чт" not in message.text and "пт" not in message.text and "сб" not in message.text and "вс" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (" + today + ")" "\n\n13:05-14:25 — ООП\n14:30-15:50 — ООП", reply_to_message_id = message.message_id)
					elif "понедельник" in message.text or "пн" in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						if message.from_user.id in first_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (понедельник)\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
						elif message.from_user.id in second_group_eng.values():
							bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (понедельник)\n\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.", reply_to_message_id = message.message_id)
					elif "вторник" in message.text or "вт" in message.text and "понедельник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (вторник)\n\nпар нет", reply_to_message_id = message.message_id)
					elif "среда" in message.text or "среду" in message.text or "ср" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (среда)\n\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.", reply_to_message_id = message.message_id)
					elif "четверг" in message.text or "чт" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (четверг)\n\n13:05-14:25 — ООП", reply_to_message_id = message.message_id)
					elif "пятница" in message.text or "пятницу" in message.text or "пт" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "суббота" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (пятница)\n\n13:05-14:25 — ООП\n14:30-15:50 — ООП", reply_to_message_id = message.message_id)
					elif "суббота" in message.text or "субботу" in message.text or "сб" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "воскресенье" not in message.text and "среду" not in message.text and "пятницу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (суббота)\n\nпар нет", reply_to_message_id = message.message_id)
					elif "воскресенье" in message.text or "вс" in message.text and "понедельник" not in message.text and "вторник" not in message.text and "среда" not in message.text and "четверг" not in message.text and "пятница" not in message.text and "суббота" not in message.text and "среду" not in message.text and "пятницу" not in message.text and "субботу" not in message.text:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (воскресенье)\n\nвоскресенье, пар нет", reply_to_message_id = message.message_id)
				elif message.from_user.id not in all_students.values():
					bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id = message.message_id)
		if "schedule" in message.text:
			if message.from_user.id in first_group.values():
				if message.from_user.id in first_group_eng.values():
					bot.send_message(message.chat.id, student_group + " группа" + " / " + week + " неделя" + "\n\nпонедельник\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.\n\nвторник\nпар нет\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n11:40-13:00 — ООП\n13:05-14:25 — ООП\n\nпятница\nпар нет")
				elif message.from_user.id in second_group_eng.values():
					bot.send_message(message.chat.id, student_group + " группа" + " / " + week + " неделя" + "\n\nпонедельник\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.\n\nвторник\nпар нет\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n11:40-13:00 — ООП\n13:05-14:25 — ООП\n\nпятница\nпар нет")
			elif message.from_user.id in second_group.values():
				if message.from_user.id in first_group_eng.values():
					bot.send_message(message.chat.id, student_group + " группа" + " / " + week + " неделя" + "\n\nпонедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n11:40-13:00 — АНГЛ. ЯЗ.\n\nвторник\nпар нет\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n13:05-14:25 — ООП\n\nпятница\n13:05-14:25 — ООП\n14:30-15:50 — ООП")
				elif message.from_user.id in second_group_eng.values():
					bot.send_message(message.chat.id, student_group + " группа" + " / " + week + " неделя" + "\n\nпонедельник\n08:30-09:50 — ВЫЧИСЛ. МАТ.\n10:00-11:20 — ВЫЧИСЛ. МАТ.\n13:05-14:25 — АНГЛ. ЯЗ.\n\nвторник\nпар нет\n\nсреда\n11:40-13:00 — ТЕОР. ВЕР.\n13:05-14:25 — ТЕОР. ВЕР.\n\nчетверг\n13:05-14:25 — ООП\n\nпятница\n13:05-14:25 — ООП\n14:30-15:50 — ООП")
			elif message.from_user.id not in all_students.values():
				bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id = message.message_id)
bot.polling()

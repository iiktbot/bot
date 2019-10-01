import date
from datetime import datetime, timedelta
import telebot
from telebot import types

bot = telebot.TeleBot('642122532:AAGKg4s2_ffJqDNTrqvbI7-qeFRxNEOBPV8')

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'привет, чем могу быть полезен?')

@bot.message_handler(content_types=['text'])
def predefined_commands(message):
	first_group = {('Виталий'):405299021, ('Юля'):393708492, ('Андрей'):416924459, ('Влад'):613759219, ('Женя'):548116631, ('Карина'):379537100, ('Денис'):635991556, ('Дима'):349737926, ('Дима'):451287655, ('Степан'):469338261, ('Денис'):542413243, ('Женя'):692445612, ('Полина'):123456789, ('Саша'):52960692}
	second_group = {('Илья'):358734682, ('Саша'):537784508, ('Богдан'):448401733, ('Влад'):643705130, ('Леша'):605903256, ('Олег'):384343953, ('Влад'):655298761, ('Дима'):384173347, ('Денис'):780853105}
	all_students = {**first_group, **second_group}
	weeknum = date.today().isocalendar()[1]
	if (weeknum % 2) == 0:
		weekorder = True
		week = "светлая"
	else:
		weekorder = False
		week = "тёмная"
	if "какая" in message.text and "неделя" in message.text:
		bot.send_message(message.chat.id, "сейчас " + week + " неделя", reply_to_message_id = message.message_id)
	for name, identifier in all_students.items():
		if identifier == message.from_user.id:
			student_name = name
	for name, identifier in first_group.items():
		if identifier == message.from_user.id:
			student_group = "первая"
	for name, identifier in second_group.items():
		if identifier == message.from_user.id:
			student_group = "вторая"
	if weekorder == True:
		if date.today().weekday() == 0 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня светлый понедельник", reply_to_message_id = message.message_id)
		elif date.today().weekday() == 1 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня светлый вторник", reply_to_message_id = message.message_id)
		elif date.today().weekday() == 2 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня светлая среда", reply_to_message_id = message.message_id)
		elif date.today().weekday() == 3 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня светлый четверг", reply_to_message_id = message.message_id)
		elif date.today().weekday() == 4 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня светлая пятница", reply_to_message_id = message.message_id)
		if "сегодня" in message.text and "вчера" not in message.text and "завтра" not in message.text:
			if "пары" in message.text or "на сколько" in message.text or "парам" in message.text or "расписание" in message.text or "расписанию" in message.text or "предметы" in message.text or "предметам" in message.text or "у нас завтра" in message.text:
				if message.from_user.id in first_group.values():
					if date.today().weekday() == 0:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n10:00 - 11:20 - вычислительная математика\n11:40 - 13:00 - английский язык", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\nвторник, пар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n11:40 - 13:00 - теория вероятностей\n13:05 - 14:25 - теория вероятностей", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n11:40 - 13:00 - объектно-ориентированное программирование\n13:05 - 14:25 - объектно-ориентированное программирование", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n08:30 - 09:50 - компьютерная схемотехника\n10:00 - 11:20 - компьютерная схемотехника", reply_to_message_id = message.message_id)
				elif message.from_user.id in second_group.values():
					if date.today().weekday() == 0:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n10:00 - 11:20 - вычислительная математика\n13:05 - 14:25 - английский язык", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\nвторник, пар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n11:40 - 13:00 - теория вероятностей\n13:05 - 14:25 - теория вероятностей", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n11:40 - 13:00 - объектно-ориентированное программирование\n13:05 - 14:25 - объектно-ориентированное программирование", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n10:00 - 11:20 - компьютерная схемотехника\n13:05 - 14:25 - компьютерная схемотехника", reply_to_message_id = message.message_id)
				else:
					bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id = message.message_id)
		elif "завтра" in message.text and "вчера" not in message.text and "сегодня" not in message.text:
			if "пары" in message.text or "на сколько" in message.text or "парам" in message.text or "расписание" in message.text or "расписанию" in message.text or "предметы" in message.text or "предметам" in message.text or "у нас завтра" in message.text:
				if message.from_user.id in first_group.values():
					if date.today().weekday() + 1 == 7:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\n10:00 - 11:20 - вычислительная математика\n11:40 - 13:00 - английский язык", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\nвторник, пар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\n11:40 - 13:00 - теория вероятностей\n13:05 - 14:25 - теория вероятностей", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\n11:40 - 13:00 - объектно-ориентированное программирование\n13:05 - 14:25 - объектно-ориентированное программирование", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\n08:30 - 09:50 - компьютерная схемотехника\n10:00 - 11:20 - компьютерная схемотехника", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 5:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\nсуббота, пар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 6:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\nвоскресенье, пар нет", reply_to_message_id = message.message_id)
				elif message.from_user.id in second_group.values():
					if date.today().weekday() + 1 == 7:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\n10:00 - 11:20 - вычислительная математика\n13:05 - 14:25 - английский язык", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\nвторник, пар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\n11:40 - 13:00 - теория вероятностей\n13:05 - 14:25 - теория вероятностей", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\n11:40 - 13:00 - объектно-ориентированное программирование\n13:05 - 14:25 - объектно-ориентированное программирование", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\n10:00 - 11:20 - компьютерная схемотехника\n13:05 - 14:25 - компьютерная схемотехника", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 5:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\nсуббота, пар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 6:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\nвоскресенье, пар нет", reply_to_message_id = message.message_id)
				else:
					bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id = message.message_id)
		elif "сегодня" not in message.text and "вчера" not in message.text and "завтра" not in message.text:
			if "пары" in message.text or "на сколько" in message.text or "парам" in message.text or "расписание" in message.text or "расписанию" in message.text or "предметы" in message.text or "предметам" in message.text or "у нас завтра" in message.text:
				if message.from_user.id in first_group.values():
					if date.today().weekday() == 0:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n10:00 - 11:20 - вычислительная математика\n11:40 - 13:00 - английский язык", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\nвторник, пар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n11:40 - 13:00 - теория вероятностей\n13:05 - 14:25 - теория вероятностей", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n11:40 - 13:00 - объектно-ориентированное программирование\n13:05 - 14:25 - объектно-ориентированное программирование", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n08:30 - 09:50 - компьютерная схемотехника\n10:00 - 11:20 - компьютерная схемотехника", reply_to_message_id = message.message_id)
				elif message.from_user.id in second_group.values():
					if date.today().weekday() == 0:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n10:00 - 11:20 - вычислительная математика\n13:05 - 14:25 - английский язык", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\nвторник, пар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n11:40 - 13:00 - теория вероятностей\n13:05 - 14:25 - теория вероятностей", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n11:40 - 13:00 - объектно-ориентированное программирование\n13:05 - 14:25 - объектно-ориентированное программирование", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n10:00 - 11:20 - компьютерная схемотехника\n13:05 - 14:25 - компьютерная схемотехника", reply_to_message_id = message.message_id)
				else:
					bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id = message.message_id)
		if "/schedule" in message.text or "/schedule@IIKTBot" in message.text:
			if message.from_user.id in first_group.values():
				bot.send_message(message.chat.id, student_group + " группа" + " / " + week + " неделя" + "\n\nпонедельник\n10:00 - 11:20 - вычислительная математика\n11:40 - 13:00 - английский язык\n\nвторник\nпар нет\n\nсреда\n11:40 - 13:00 - теория вероятностей\n13:05 - 14:25 - теория вероятностей\n\nчетверг\n11:40 - 13:00 - объектно-ориентированное программирование\n13:05 - 14:25 - объектно-ориентированное программирование\n\nпятница\n08:30 - 09:50 - компьютерная схемотехника\n10:00 - 11:20 - компьютерная схемотехника")
			elif message.from_user.id in second_group.values():
				bot.send_message(message.chat.id, student_group + " группа" + " / " + week + " неделя" + "\n\nпонедельник\n10:00 - 11:20 - вычислительная математика\n13:05 - 14:25 - английский язык\n\nвторник\nпар нет\n\nсреда\n11:40 - 13:00 - теория вероятностей\n13:05 - 14:25 - теория вероятностей\n\nчетверг\n11:40 - 13:00 - объектно-ориентированное программирование\n13:05 - 14:25 - объектно-ориентированное программирование\n\nпятница\n10:00 - 11:20 - компьютерная схемотехника\n13:05 - 14:25 - компьютерная схемотехника")
			else:
				bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id = message.message_id)
	elif weekorder == False:
		if date.today().weekday() == 0 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня тёмный понедельник", reply_to_message_id = message.message_id)
		elif date.today().weekday() == 1 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня тёмный вторник", reply_to_message_id = message.message_id)
		elif date.today().weekday() == 2 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня тёмная среда", reply_to_message_id = message.message_id)
		elif date.today().weekday() == 3 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня тёмный четверг", reply_to_message_id = message.message_id)
		elif date.today().weekday() == 4 and "какой" in message.text and "день" in message.text:
			bot.send_message(message.chat.id, "сегодня тёмная пятница", reply_to_message_id = message.message_id)
		if "сегодня" in message.text and "вчера" not in message.text and "завтра" not in message.text:
			if "пары" in message.text or "на сколько" in message.text or "парам" in message.text or "расписание" in message.text or "расписанию" in message.text or "предметы" in message.text or "предметам" in message.text or "у нас завтра" in message.text:
				if message.from_user.id in first_group.values():
					if date.today().weekday() == 0:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n08:30 - 09:50 - вычислительная математика\n10:00 - 11:20 - вычислительная математика\n11:40 - 13:00 - английский язык", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\nвторник, пар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n11:40 - 13:00 - теория вероятностей\n13:05 - 14:25 - теория вероятностей", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n11:40 - 13:00 - объектно-ориентированное программирование\n13:05 - 14:25 - объектно-ориентированное программирование", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\nпятница, пар нет", reply_to_message_id = message.message_id)
				elif message.from_user.id in second_group.values():
					if date.today().weekday() == 0:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n08:30 - 09:50 - вычислительная математика\n10:00 - 11:20 - вычислительная математика\n13:05 - 14:25 - английский язык", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\nвторник, пар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n11:40 - 13:00 - теория вероятностей\n13:05 - 14:25 - теория вероятностей", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n11:40 - 13:00 - объектно-ориентированное программирование", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n13:05 - 14:25 - объектно-ориентированное программирование\n14:30 - 15:50 - объектно-ориентированное программирование", reply_to_message_id = message.message_id)
				else:
					bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id = message.message_id)
		elif "завтра" in message.text and "вчера" not in message.text and "сегодня" not in message.text:
			if "пары" in message.text or "на сколько" in message.text or "парам" in message.text or "расписание" in message.text or "расписанию" in message.text or "предметы" in message.text or "предметам" in message.text or "у нас завтра" in message.text:
				if message.from_user.id in first_group.values():
					if date.today().weekday() + 1 == 7:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\n08:30 - 09:50 - вычислительная математика\n10:00 - 11:20 - вычислительная математика\n11:40 - 13:00 - английский язык", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\nвторник, пар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\n11:40 - 13:00 - теория вероятностей\n13:05 - 14:25 - теория вероятностей", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\n11:40 - 13:00 - объектно-ориентированное программирование\n13:05 - 14:25 - объектно-ориентированное программирование", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\nпятница, пар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 5:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\nсуббота, пар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 6:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\nвоскресенье, пар нет", reply_to_message_id = message.message_id)
				elif message.from_user.id in second_group.values():
					if date.today().weekday() + 1 == 7:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\n08:30 - 09:50 - вычислительная математика\n10:00 - 11:20 - вычислительная математика\n13:05 - 14:25 - английский язык", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\nвторник, пар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\n11:40 - 13:00 - теория вероятностей\n13:05 - 14:25 - теория вероятностей", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\n11:40 - 13:00 - объектно-ориентированное программирование", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\n13:05 - 14:25 - объектно-ориентированное программирование\n14:30 - 15:50 - объектно-ориентированное программирование", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 5:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\nсуббота, пар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() + 1 == 6:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на завтра)\n\nвоскресенье, пар нет", reply_to_message_id = message.message_id)
				else:
					bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id = message.message_id)
		elif "сегодня" not in message.text and "вчера" not in message.text and "завтра" not in message.text:
			if "пары" in message.text or "на сколько" in message.text or "парам" in message.text or "расписание" in message.text or "расписанию" in message.text or "предметы" in message.text or "предметам" in message.text or "у нас завтра" in message.text:
				if message.from_user.id in first_group.values():
					if date.today().weekday() == 0:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n08:30 - 09:50 - вычислительная математика\n10:00 - 11:20 - вычислительная математика\n11:40 - 13:00 - английский язык", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\nвторник, пар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n11:40 - 13:00 - теория вероятностей\n13:05 - 14:25 - теория вероятностей", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n11:40 - 13:00 - объектно-ориентированное программирование\n13:05 - 14:25 - объектно-ориентированное программирование", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\nпятница, пар нет", reply_to_message_id = message.message_id)
				elif message.from_user.id in second_group.values():
					if date.today().weekday() == 0:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n08:30 - 09:50 - вычислительная математика\n10:00 - 11:20 - вычислительная математика\n13:05 - 14:25 - английский язык", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 1:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\nвторник, пар нет", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 2:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n11:40 - 13:00 - теория вероятностей\n13:05 - 14:25 - теория вероятностей", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 3:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n11:40 - 13:00 - объектно-ориентированное программирование", reply_to_message_id = message.message_id)
					elif date.today().weekday() == 4:
						bot.send_message(message.chat.id, student_name + ", " + student_group + " группа" + " (на сегодня)\n\n13:05 - 14:25 - объектно-ориентированное программирование\n14:30 - 15:50 - объектно-ориентированное программирование", reply_to_message_id = message.message_id)
				else:
					bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id = message.message_id)
		if "/schedule" in message.text or "/schedule@IIKTBot" in message.text:
			if message.from_user.id in first_group.values():
				bot.send_message(message.chat.id, student_group + " группа" + " / " + week + " неделя" + "\n\nпонедельник\n08:30 - 09:50 - вычислительная математика\n10:00 - 11:20 - вычислительная математика\n11:40 - 13:00 - английский язык\n\nвторник\nпар нет\n\nсреда\n11:40 - 13:00 - теория вероятностей\n13:05 - 14:25 - теория вероятностей\n\nчетверг\n11:40 - 13:00 - объектно-ориентированное программирование\n13:05 - 14:25 - объектно-ориентированное программирование\n\nпятница\nпар нет")
			elif message.from_user.id in second_group.values():
				bot.send_message(message.chat.id, student_group + " группа" + " / " + week + " неделя" + "\n\nпонедельник\n08:30 - 09:50 - вычислительная математика\n10:00 - 11:20 - вычислительная математика\n13:05 - 14:25 - английский язык\n\nвторник\nпар нет\n\nсреда\n11:40 - 13:00 - теория вероятностей\n13:05 - 14:25 - теория вероятностей\n\nчетверг\n11:40 - 13:00 - объектно-ориентированное программирование\n\nпятница\n13:05 - 14:25 - объектно-ориентированное программирование\n14:30 - 15:50 - объектно-ориентированное программирование")
			else:
				bot.send_message(message.chat.id, "вряд ли ты здесь учишься", reply_to_message_id = message.message_id)
bot.polling()

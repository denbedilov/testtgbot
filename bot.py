# -*- coding: utf-8 -*-
import config
import telebot
import random

from time import gmtime, strftime

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
	if message.text == '/амелия':
		bot.send_message(message.chat.id, 'Амелия начинает расстрел чата! Тра-та-та-та!! ' + get_user_name() + ' убит, помянем его')
	if 'нахуй' in message.text or 'бля' in message.text:
		bot.delete_message(message.chat.id, message.message_id)
#	if message.text == 'Стикеры для геев':
#		bot.send_message(message.chat.id, "ЗАТКНИСЬ БОТ")	
	if message.text == 'который час?':
		bot.reply_to(message, strftime("%H:%M:%S", gmtime()))

#@bot.message_handler(content_types = ["sticker"])
#def stiker_reply(message):
#	bot.reply_to(message, "Стикеры НЕ для геев")		

#	else:
#		bot.send_message(message.chat.id, message.text)

def get_user_name():
	return config.users[random.randint(0,len(config.users)-1)]

if __name__ == '__main__':
	bot.polling(none_stop=True)

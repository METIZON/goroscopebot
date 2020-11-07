# -*- coding: utf8 -*-

import telebot
import requests
from bs4 import BeautifulSoup
import datetime

# t.me/TrueGoroscope_bot
# telegram: t.me/metiz0n

try:
    bot = telebot.TeleBot('1261892119:AAFEu69hz2xQdxH1h8KuqlJuZuVD0ygUj_c')

    markup1 = telebot.types.InlineKeyboardMarkup()

    oven = telebot.types.InlineKeyboardButton(text='♈Овен♈',
                                              callback_data='oven')
    telec = telebot.types.InlineKeyboardButton(text='♉Телец♉',
                                               callback_data='telec')
    bliznec = telebot.types.InlineKeyboardButton(text='♊Близнец♊',
                                                 callback_data='bliznec')
    rak = telebot.types.InlineKeyboardButton(text='♋Рак♋',
                                             callback_data='rak')
    lev = telebot.types.InlineKeyboardButton(text='♌Лев♌',
                                             callback_data='lev')
    deva = telebot.types.InlineKeyboardButton(text='♍Дева♍',
                                              callback_data='deva')
    vesy = telebot.types.InlineKeyboardButton(text='♎Весы♎',
                                              callback_data='vesy')
    skorpion = telebot.types.InlineKeyboardButton(text='♏Скорпион♏',
                                                  callback_data='scorpion')
    strelec = telebot.types.InlineKeyboardButton(text='♐Стрелец♐',
                                                 callback_data='strelec')
    kozerog = telebot.types.InlineKeyboardButton(text='♑Козерог♑',
                                                 callback_data='kozerog')
    aqua = telebot.types.InlineKeyboardButton(text='♒Водолей♒',
                                              callback_data='aqua')
    fish = telebot.types.InlineKeyboardButton(text='♓Рыбы♓',
                                              callback_data='fish')

    markup1.add(oven, telec)
    markup1.add(bliznec, rak)
    markup1.add(lev, deva)
    markup1.add(vesy, skorpion)
    markup1.add(strelec, kozerog)
    markup1.add(aqua, fish)

    @bot.message_handler(commands=['start'])
    def start_msg(message):
        bot.send_message(message.chat.id,
                         text=f'Приветствую {message.chat.first_name}! Выберите ваш знак зодиака:',
                         reply_markup=markup1)

    @bot.message_handler(content_types=['text'])
    def send_msg(message):
        if message.text:
            bot.send_message(message.chat.id,
                             'Ссылка на бота: '
                             't.me/TrueGoroscope_bot')

    @bot.callback_query_handler(func=lambda call: True)
    def query_handler(call):
        if call.data == 'oven':
            res = requests.get(
                'https://orakul.com/horoscope/astrologic/general/aries/today.html').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[1] + '.' + b[2] + ':\n ' + info[0])
        elif call.data == 'telec':
            res = requests.get(
                'https://orakul.com/horoscope/astrologic/general/taurus/today.html').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[1] + '.' + b[2] + ':\n ' + info[0])
        elif call.data == 'bliznec':
            res = requests.get(
                'https://orakul.com/horoscope/astrologic/general/gemini/today.html').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[1] + '.' + b[2] + ':\n ' + info[0])
        elif call.data == 'rak':
            res = requests.get(
                'https://orakul.com/horoscope/astrologic/general/cancer/today.html').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[1] + '.' + b[2] + ':\n ' + info[0])
        elif call.data == 'lev':
            res = requests.get(
                'https://orakul.com/horoscope/astrologic/general/lion/today.html').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[1] + '.' + b[2] + ':\n ' + info[0])
        elif call.data == 'deva':
            res = requests.get(
                'https://orakul.com/horoscope/astrologic/general/virgo/today.html').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[1] + '.' + b[2] + ':\n ' + info[0])
        elif call.data == 'vesy':
            res = requests.get(
                'https://orakul.com/horoscope/astrologic/general/libra/today.html').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[1] + '.' + b[2] + ':\n ' + info[0])
        elif call.data == 'scorpion':
            res = requests.get(
                'https://orakul.com/horoscope/astrologic/general/scorpio/today.html').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[1] + '.' + b[2] + ':\n ' + info[0])
        elif call.data == 'strelec':
            res = requests.get(
                'https://orakul.com/horoscope/astrologic/general/sagittarius/today.html').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[1] + '.' + b[2] + ':\n ' + info[0])
        elif call.data == 'kozerog':
            res = requests.get(
                'https://orakul.com/horoscope/astrologic/general/capricorn/today.html').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[1] + '.' + b[2] + ':\n ' + info[0])
        elif call.data == 'aqua':
            res = requests.get(
                'https://orakul.com/horoscope/astrologic/general/aquarius/today.html').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[1] + '.' + b[2] + ':\n ' + info[0])
        elif call.data == 'fish':
            res = requests.get(
                'https://orakul.com/horoscope/astrologic/general/pisces/today.html').text
            soup = BeautifulSoup(res, features="html.parser")
            soup.encode('utf-8')
            cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
            info = cases.split('Подробнее')
            a = str(datetime.date.today())
            b = a.split('-')
            bot.send_message(
                call.message.chat.id, 'Ваш гороскоп на ' + b[1] + '.' + b[2] + ':\n ' + info[0])
        else:
            pass

    bot.polling(none_stop=True)
except Exception:
    pass

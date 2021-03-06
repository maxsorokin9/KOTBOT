#все требуемые библиотеки для самого бота, создания кнопки и выдачи рандоных файлов
from glob import glob
from random import choice
from telebot import apihelper, types

import telebot
#инициируем самого бота
apihelper.proxy = {'https': 'socks5://learn:python@t2.learn.python.ru:1080'}
bot = telebot.TeleBot("1289356561:AAFFY7K5sG4leLErxmIfR5HRk2dy51vMbV8")


#создаем кнопку командной строки
markup = types.ReplyKeyboardMarkup(row_width=1)
item = types.KeyboardButton('Получить')
markup.row(item)

#начало общения в боте
@bot.message_handler(commands=['start'])
def start(message):
    user = message.chat.id
    bot.send_message(
        user, "Хочешь фото котика?", reply_markup=markup
        )

#ответ на запрос по кнопке, бот будет выдавать рандомные файлы из папки, начинающиеся с 'cat'
@bot.message_handler(regexp='Получить')
def send_picture(message):
    user = message.chat.id
    cat_list = glob('images/cat*.jp*g')
    cat_pic = choice(cat_list)
    bot.send_photo(user, open(cat_pic, 'rb'))
    bot.send_message(
        user, "Еще?...", reply_markup=markup
        )


bot.polling()

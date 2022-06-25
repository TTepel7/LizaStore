# Библиотеки
from unicodedata import name
from sympy import false, true
import telebot
import yadisk
#import database
import os
from peewee import *


# Подключаемся к Я.Диску и проверяем токен
y = yadisk.YaDisk(token="AQAAAABicHdlAAgCbDVt0snMj0oCnjhFKbp8Uh4")
y.check_token()


# Подключаемся к боту по токену
bot = telebot.TeleBot('5313426341:AAFM1oAtKlDGmyFVzmrWPAfSVlovGL59vO4')


# Реакция на команду старт
@bot.message_handler(commands=["добавить"])
def start(m, res=False):

    mesg = bot.send_message(
        m.chat.id, "Приветствую,{0}! Отправьте файл".format(m.from_user.username))

    bot.register_next_step_handler(mesg, handle_docs_photo)


# Реакция на отправку картинки(документа)
@bot.message_handler(content_types=['document,photo'])
def handle_docs_photo(message):
    try:

        # Получаем отправленый файл
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)  # Качаем файл

        src = 'temp/' + message.document.file_name  # Как и куда будет записыватся файл
        with open(src, 'wb') as new_file:  # Создание фаила во временной папке
            new_file.write(downloaded_file)

        y.upload('temp/{0}'.format(message.document.file_name),
                 'LAbot/{0}'.format(message.document.file_name))  # Загрузка фаила на Я.Диск
        b = y.publish('LAbot/{0}'.format(message.document.file_name))   
              
        # Удаление фаила из временной папки
        os.remove('temp/{0}'.format(message.document.file_name))

        # Уведомляем о том что фаил  загружен 'Фаил загружен! Теоретически....' и даём ссылку на файл
        bot.reply_to(message, 'Файл загружен! Теоретически....Ссылка:{0}'.format( y.get_download_link('LAbot/{0}'.format(message.document.file_name))))
        
        
        

    except Exception as e:
        bot.reply_to(message, e)


print('Бот запущен')
bot.polling(none_stop=True, interval=0)  # Запуск бота

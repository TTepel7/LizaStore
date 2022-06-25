# Библиотеки
from unicodedata import name
from sympy import false, true
import telebot
import yadisk
#import database
import os
from PIL import Image
from PIL.ExifTags import TAGS

# Подключаемся к Я.Диску и проверяем токен
y = yadisk.YaDisk(token="AQAAAABicHdlAAgCbDVt0snMj0oCnjhFKbp8Uh4")
y.check_token()


# Подключаемся к боту по токену
bot = telebot.TeleBot('5313426341:AAFM1oAtKlDGmyFVzmrWPAfSVlovGL59vO4')


# Реакция на команду старт
@bot.message_handler(commands=["start"])
def start(m, res=False):

    mesg = bot.send_message(
        m.chat.id, "Приветствую,{0}! Отправьте файл".format(m.from_user.username))

    bot .register_next_step_handler(mesg, handle_docs_photo)


# Реакция на отправку картинки(документа)
@bot.message_handler(content_types=['document', 'photo', 'text'])
def handle_docs_photo(message):
    try:

        if message.content_type == 'document':
            # Получаем отправленый файл
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(
                file_info.file_path)  # Качаем файл

            src = 'temp/' + message.document.file_name  # Как и куда будет записыватся файл
            with open(src, 'wb') as new_file:  # Создание фаила во временной папке
                new_file.write(downloaded_file)

            y.upload('temp/{0}'.format(message.document.file_name),
                     'LAbot/{0}'.format(message.document.file_name))  # Загрузка фаила на Я.Диск

            b = y.publish('LAbot/{0}'.format(message.document.file_name))

            # Удаление фаила из временной папки
            os.remove('temp/{0}'.format(message.document.file_name))

            # Уведомляем о том что фаил  загружен 'Фаил загружен! Теоретически....' и даём ссылку на файл

            bot.reply_to(message, 'Файл загружен!')

            # return handle_docs_photo
            bot .register_next_step_handler(bot.send_message(
                message.chat.id, 'Загрузите следующее изображение, чтобы выйти из режима загрузки введите любое текстове сообщение'), handle_docs_photo)

        elif message.content_type == 'text':
            bot.send_message(
                message.chat.id, "Режим загрузки файлов выключен, чтобы начать вновь, введите команду start")

    except Exception as e:
        bot.reply_to(message, e)


print('Бот запущен')
bot.polling(none_stop=True, interval=1)  # Запуск бота

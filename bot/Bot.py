# Библиотеки
from unicodedata import name
from sympy import false, true
import telebot
import yadisk
#import database
import os
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

# Подключаемся к Я.Диску и проверяем токен
y = yadisk.YaDisk(token="AQAAAABicHdlAAgCbDVt0snMj0oCnjhFKbp8Uh4")
y.check_token()


# Подключаемся к боту по токену
bot = telebot.TeleBot('5313426341:AAFM1oAtKlDGmyFVzmrWPAfSVlovGL59vO4')


#Реакция на команду старт
@bot.message_handler(commands=["start"])
def start(m,res=False):

    mesg = bot.send_message(
        m.chat.id, "Приветствую,{0}! Отправьте файл".format(m.from_user.username))

    bot .register_next_step_handler(mesg, handle_docs_photo)


# Реакция на отправку картинки(документа)
@bot.message_handler(content_types=['document,photo','text'])
def handle_docs_photo(message):
    try:

        if message.content_type == 'document':
                # Получаем отправленый файл
                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)  # Качаем файл

                src = 'temp/' + message.document.file_name  # Как и куда будет записыватся файл
                with open(src, 'wb') as new_file:  # Создание фаила во временной папке
                    new_file.write(downloaded_file)

                y.upload('temp/{0}'.format(message.document.file_name),
                        'LAbot/{0}'.format(message.document.file_name))  # Загрузка фаила на Я.Диск
                b = y.publish('LAbot/{0}'.format(message.document.file_name))
                getex = get_exif('temp/{0}'.format(message.document.file_name))   
                bot.reply_to(message, getex['DateTimeOriginal'])    
                # Удаление фаила из временной папки
                os.remove('temp/{0}'.format(message.document.file_name))

                # Уведомляем о том что фаил  загружен 'Фаил загружен! Теоретически....' и даём ссылку на файл
                #bot.reply_to(message, 'Файл загружен! Теоретически....Ссылка:{0}'.format( y.get_download_link('LAbot/{0}'.format(message.document.file_name))))
                bot.reply_to(message, 'Файл загружен!')
                
                #return handle_docs_photo
                bot .register_next_step_handler(bot.send_message(message.chat.id,'Загрузите следующее изображение, чтобы выйти из режима загрузки введите любое текстове сообщение'), handle_docs_photo)
        
        
        elif message.content_type == 'photo':
            # Получаем отправленый файл
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)  # Качаем файл

            src = 'temp/' + message.photo[1].file_id  # Как и куда будет записыватся файл
            with open(src, 'wb') as new_file:  # Создание фаила во временной папке
                new_file.write(downloaded_file)

            y.upload('temp/{0}'.format(message.photo[1].file_id),
                    'LAbot/{0}'.format(message.photo[1].file_id))  # Загрузка фаила на Я.Диск
            b = y.publish('LAbot/{0}'.format(message.photo[1].file_id))
            getex = get_exif('temp/{0}'.format(message.photo[1].file_id))   
            bot.reply_to(message, getex['DateTimeOriginal'])     
                
            # Удаление фаила из временной папки
            os.remove('temp/{0}'.format(message.photo[1].file_id))

            # Уведомляем о том что фаил  загружен 'Фаил загружен! Теоретически....' и даём ссылку на файл
            #bot.reply_to(message, 'Файл загружен! Теоретически....Ссылка:{0}'.format( y.get_download_link('LAbot/{0}'.format(message.photo[1].file_id))))
            bot.reply_to(message, 'Файл загружен!')
            bot .register_next_step_handler(bot.send_message(message.chat.id,'Загрузите следующее изображение, чтобы выйти из режима загрузки введите любое текстове сообщение'), handle_docs_photo)
        elif message.content_type == 'text':
            bot.send_message(message.chat.id,"Режим загрузки файлов выключен, чтобы начать вновь, введите команду start")

    except Exception as e:
        bot.reply_to(message, e)


print('Бот запущен')
bot.polling(none_stop=True, interval= 1)  # Запуск бота


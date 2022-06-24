# Библиотеки
import telebot
import yadisk
import sys
import os


# Подключаемся к Я.Диску и проверяем токен
y = yadisk.YaDisk(token="AQAAAABicHdlAAgCbDVt0snMj0oCnjhFKbp8Uh4")
y.check_token()




# Подключаемся к боту по токену
bot = telebot.TeleBot('5313426341:AAFM1oAtKlDGmyFVzmrWPAfSVlovGL59vO4')

# Реакция на команду старт
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправь фотографию, и я её загружу )')

# Реакция на отправку картинки(документа)
@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    try:
        
        file_info = bot.get_file(message.document.file_id) # Получаем отправленый фаил
        downloaded_file = bot.download_file(file_info.file_path) # Качаем фаил

        src = 'temp/' + message.document.file_name #Как и куда будет записыватся фаил
        with open(src, 'wb') as new_file: #Создание фаила во временной папке
            new_file.write(downloaded_file)

        y.upload('temp/{0}'.format(message.document.file_name),'LAbot/{0}'.format(message.document.file_name))#Загрузка фаила на Я.Диск
        os.remove('temp/{0}'.format(message.document.file_name))#Удаление фаила из временной папки

       
        bot.reply_to(message,'Фаил загружен! Теоретически....')#Уведомляем о том что фаил  загружен
    except Exception as e:
        bot.reply_to(message, e)

# %%
bot.polling(none_stop=True, interval=0) #Запуск бота



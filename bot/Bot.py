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
@bot.message_handler(commands=["start"])
def start(m, res=False):
    #users = Person.select()
    #users_prem = []
    # for i in users:
    #     users_prem.append(i.tele_name)
    # if m.from_user.username not in users_prem:
    #     bot.send_message(m.chat.id, "Отказано в доступе!")
    # else:
        mesg = bot.send_message(m.chat.id, "Приветствую,{0}!".format(m.from_user.username))
        # global auto_flag
        # auto_flag = true
        #bot.send_message(m.chat.id, auto_flag)
        #q_admin = Person.select().where(Person.role == 'Admin' and Person.tele_name == '{0}'.format(m.from_user.username))
        # if q_admin:
        #     global admin_flag
        #     admin_flag = true
        bot.register_next_step_handler(mesg,handle_docs_photo)
        
        



# Реакция на отправку картинки(документа)
@bot.message_handler(content_types=['document,photo'])
def handle_docs_photo(message):
    try:
            
            file_info = bot.get_file(message.document.file_id) # Получаем отправленый файл
            downloaded_file = bot.download_file(file_info.file_path) # Качаем файл

            src = 'temp/' + message.document.file_name #Как и куда будет записыватся файл
            with open(src, 'wb') as new_file: #Создание фаила во временной папке
                new_file.write(downloaded_file)

            y.upload('temp/{0}'.format(message.document.file_name),'LAbot/{0}'.format(message.document.file_name))#Загрузка фаила на Я.Диск
            os.remove('temp/{0}'.format(message.document.file_name))#Удаление фаила из временной папки

        
            bot.reply_to(message,'Фаил загружен! Теоретически....')#Уведомляем о том что фаил  загружен 'Фаил загружен! Теоретически....'


            # if message.content_type == 'photo':
            #     file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            #     downloaded_file = bot.download_file(file_info.file_path)
            #     src = 'temp/' + message.document.file_name
            #     with open(src, 'wb') as new_file:
            #         new_file.write(downloaded_file)
            #     y.upload('temp/{0}'.format(message.document.file_name),'LAbot/{0}'.format(message.document.file_name))#Загрузка фаила на Я.Диск
            #     os.remove('temp/{0}'.format(message.document.file_name))#Удаление фаила из временной папки

        
            #     bot.reply_to(message,'Фаил загружен! Теоретически....')#Уведомляем о том что фаил  загружен 'Фаил загружен! Теоретически....'

            # elif message.content_type == 'document':
            #     file_info = bot.get_file(message.document.file_id)
            #     downloaded_file = bot.download_file(file_info.file_path)
            #     src = 'temp/' + message.document.file_name
            #     with open(src, 'wb') as new_file:
            #         new_file.write(downloaded_file)
            #     y.upload('temp/{0}'.format(message.document.file_name),'LAbot/{0}'.format(message.document.file_name))#Загрузка фаила на Я.Диск
            #     os.remove('temp/{0}'.format(message.document.file_name))#Удаление фаила из временной папки

        
            #bot.reply_to(message,'Фаил загружен! Теоретически....')#Уведомляем о том что фаил  загружен 'Фаил загружен! Теоретически....'





    except Exception as e:
            bot.reply_to(message, e)

    # if admin_flag == true:
    #     @bot.message_handler(commands=["add"])
    #     def add(message):
    #         mesg = bot.send_message(message.chat.id,'Вы добавляете пользователя. Введите телеграм пользователя(@Exemple, но без собаки) и его роль через запятую')
    #         bot.register_next_step_handler(mesg,users_add)
        
    #     def users_add(message):
    #         database.Person(tele_name = message.text.split(',')[0], role = message.text.split(',')[1])



# %%
bot.polling(none_stop=True, interval=0) #Запуск бота



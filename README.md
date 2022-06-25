<p align="center">
    <h1 align="center">Система хранения медиа материала</h1>
</p>
<h4>Реализованная функциональность</h4>
<ul>
    <li>Искусственный интеллект;</li>
    <li>Telegram-бот;</li>
    <li>Сайт с авторизацией;</li>
</ul> 
<h4>Особенность проекта в следующем:</h4>
<ul>
 <li>Выставление гео-меток фотографиям;</li>
 <li>Выставление меток времени загрузки/создания фотографий;</li>
 <li>Множественная фильтрация;</li>  
 <li>Загрзука фотографий через Telegram;</li>  
 <li>Включение/выключение редактирования результатов ИИ;</li>    
 <li>Раздел для СМИ на сайте;</li>
 </ul>
<h4>Основной стек технологий:</h4>
<ul>
    <li>Tensorflow, Keras.</li>
	<li>HTML, CSS, JavaScript</li>
	<li>PHP 7.4, MySQL.</li>
	<li>SASS/li>
	<li>Vue.js, Bootstrap 5.</li>
	<li>Git, Gitlab.</li>
	<li> Telebot, yadisk.</li>
  
 </ul>
<h4>Сайт</h4>
<p>Сайт с решением доступен по адресу: http://archive.lizaalert.xsph.ru/ </p>
<p>Реквизиты тестового пользователя: email: <b>Liza@alert.ru</b>, пароль: <b>qwerty52</b></p>




СРЕДА ЗАПУСКА
------------
Доступно на всех телефонах и ПК с доступом к сети Интернет

Подключение web-сайта
------------
для запуска необходимо в папке web/LizaWeb настроить файл `.env`, затем прописать следующиие команды

```
composer install
npm install
npm run prod
php artisan migrate --seed
php artisan serve
```

в файле env важно добавить ключи
```
YANDEX_DISK_BASE_PATH=/
YANDEX_DISK_OAUTH_TOKEN=<токен Oauth для яндекс диска>

//подключение к БД
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=lizaalert
DB_USERNAME=root
DB_PASSWORD=1234
```

### Подключение telegram-бота name

Подключение бота
------------
### Подключение telegram-бота name
1) Чтобы добавить бота в группу, при добавлении нового участника введите Liza_AlertArchive_bot
2) При подтверждении, что бот в группе, введите комманду /start. Teперь бот следит за чатом
3) Чтобы загрузить изображение в облако, отправьте его документом. Бот умеет обрабатывать несколько изображений в одном сообщении
4) Отправляйте не более 5 изображений раз в 5-7 минут
5) Отправка любого текстового сообщения останавливает бота. Для его повторного запуска выполните команду /start

Для запуска бота физически:
1) Запустите файл Bot.py с установленой библиотекой telebot
2) Для установки библиотеки telebot в командной строке Windows введите pip install telebot

Для запуска скрипта мониторинга:
1) Запустите yad_monitor.py с установленой библиотекой yadisk, и файлом model_script.py в этой же директории
~~~
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install name1
sudo apt-get install mariadb-client mariadb-server
git clone https://github.com/Sinclear/default_readme
cd default_readme
...
~~~

РАЗРАБОТЧИКИ

<h4>Пепелышев Дмитирий</h4>
<h4>Широких Арина</h4>
<h4>Демидова Анастасия</h4>
<h4>Селезнев Роман</h4>



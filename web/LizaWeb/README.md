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

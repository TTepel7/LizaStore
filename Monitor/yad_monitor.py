import yadisk
import model_script
import time
from PIL import Image
from PIL.ExifTags import TAGS
import os
import glob


def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret
#поддержка скрипта    
while True:
    try:
        # Подключаемся к Я.Диску и проверяем токен
        y = yadisk.YaDisk(token="AQAAAABicHdlAAgCbDVt0snMj0oCnjhFKbp8Uh4")
        y.check_token()

        # exif = get_exif('temp/20210417_100412.jpg')
        # print(exif['GPSInfo'][2][0])
        upload_path = 'LAbot/'

        while True:
            files = y.listdir(upload_path)
            a = []
            for i in files:
                a.append(i)
                print(i['name'])
            # print('epe')
            # break
            if len(a) != 0:

                for i in a:
                    try:
                        print('With')
                        y.download(
                            'LAbot/{0}'.format(i['name']), 'temp/{0}'.format(i['name']))
                        print('epe')
                        exif = get_exif('temp/{0}'.format(i['name']))

                        pred = model_script.predict('temp/{0}'.format(i['name']))
                        geo = exif['GPSInfo'][2]
                        model_script.to_site(
                            name=str(i['name']),
                            token=str("qwerty52"),
                            desc=str("https://www.google.ru/maps/place/{0}N+{1}E/".format(geo[0],geo[1])),
                            tele=str("@LizaAlert"),
                            disk_url=str(i['file']),
                            tags=pred
                        )
                        y.upload('temp/{0}'.format(i['name']),
                                'Predicted/{0}'.format(i['name']))  # Загрузка фаила на Я.Диск
                        y.remove('LAbot/{0}'.format(i['name']))
                        del pred,exif
                        #os.remove('temp/{0}'.format(i['name']))
                        # for file in glob.glob("temp/*"):
                        #     os.remove(file)

                    except:
                        print('Without')
                        y.remove('LAbot/{0}'.format(i['name']))

                        pred = model_script.predict('temp/{0}'.format(i['name']))

                        model_script.to_site_without(
                            name=str(i['name']),
                            token=str("qwerty52"),
                            tele=str("@LizaAlert"),
                            disk_url=str(i['file']),
                            tags=pred
                        )
                        y.upload('temp/{0}'.format(i['name']),
                                'Predicted/{0}'.format(i['name']))  # Загрузка фаила на Я.Диск
                        # for file in glob.glob("temp/*"):
                        #      os.remove(file)
                        del pred         

            else:
                for file in glob.glob("temp/*"):
                            os.remove(file) 
                print('Ожидание')
                time.sleep(30)
    except:
        continue
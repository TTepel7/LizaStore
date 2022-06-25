import tensorflow as tf
from PIL import Image
import numpy as np
import requests as re
import json




def predict(image_path):
    model = tf.keras.models.load_model('LAModel_9481.h5')

    image = np.array(Image.open(image_path).resize((256, 256)))
    images_list = []
    images_list.append(np.array(image))
    x = np.asarray(images_list)

    prediction = model.predict(x)
    arr =[]
    for i in prediction:
        for j in i:
            if j >=1:
                arr.append(j)
            elif j < 1:
                arr.append(0)
    tags = []
    for i in range(len(arr)):
         if arr[i] == 1:
            tags.append(i+1)
          
    
    return tags

#http://archive.lizaalert.xsph.ru/api/media   


def to_site(name,token,desc,tele,disk_url,tags):
    url = re.post('http://archive.lizaalert.xsph.ru/api/media',json=
    {'name':name,
    'api_token':token,
    'description':desc,
    'telegram':tele,
    'disk_url':disk_url,
    'tags':tags},headers={'Content-Type':'application/json','Accept':'application/json'})
    print(url.text)

def to_site_without(name,token,tele,disk_url,tags):
    url = re.post('http://archive.lizaalert.xsph.ru/api/media',json=
    {'name':name,
    'api_token':token,
    'telegram':tele,
    'disk_url':disk_url,
    'tags':tags},headers={'Content-Type':'application/json','Accept':'application/json'})
    print(url.text)
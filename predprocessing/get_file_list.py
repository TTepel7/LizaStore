import os
import json
# используется для получения списка файлов в json
file_list = []
for img in os.listdir("Итоговый датасет"):
    file_list.append(img)
with open('files.json','w') as f:
    f.write(json.dumps(file_list))
import os
import shutil

root_dir = os.walk('my_project')
temp = os.path.join('my_project', 'templates')
if not os.path.exists(temp):
    os.mkdir(temp)
for root, dirs, files in os.walk('my_project'):
    for file in files:
        if file.endswith('.html'):
            folder = root.split('\\')[-1]
            if not os.path.exists(os.path.join(temp, folder)):
                os.mkdir(os.path.join(temp, folder))
            shutil.copy2(os.path.join(root, file), os.path.join(temp, folder))
# Код выполняется, но выходит ошибка.
import os

with open('config.yaml', encoding='utf-8') as config:
    new_dir = ''
    i = 0
    for path in config:
        # Получаем название в чистом виде
        directory = path.strip('\n').strip('|--') if path.startswith('|--') else path.strip().strip("   |--")
        # Создаем папки и файлы
        if directory.endswith('.py') or directory.endswith('.html'):
            with open(f'{new_dir}\\{directory}', 'w', encoding='utf-8') as fw:
                fw = fw.writelines('')
        else:
            # Определяем вложенность и создаем папку
            while True:
                if path.startswith('|--'):
                    new_dir = os.path.join(new_dir, directory)
                    if not os.path.exists(new_dir):
                        os.mkdir(new_dir)
                    break
                elif path.startswith('   |--'):
                    i += 1
                    if i > 0:
                        new_dir = new_dir.split('\\').pop(0)
                    new_dir = os.path.join(new_dir, directory)
                    if not os.path.exists(new_dir):
                        os.mkdir(new_dir)
                    break
                elif path.startswith('   '):
                    path = path.strip('   ')
                elif path.startswith('|  '):
                    path = '|' + path.strip('|  ')

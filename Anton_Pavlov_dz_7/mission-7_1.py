import os

main_dir = os.path.join('my_project')
if not os.path.exists(main_dir):
    os.mkdir(main_dir)
list_dirs = ['settings', 'adminapp', 'mainapp', 'authapp']
for directory in list_dirs:
    os.path.join(main_dir, directory)
    if not os.path.exists(f'{main_dir}/{directory}'):
        os.mkdir(f'{main_dir}/{directory}')

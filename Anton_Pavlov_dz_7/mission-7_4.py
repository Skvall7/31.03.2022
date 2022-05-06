import os


def stat_dir(directory):
    dict_size = {10 ** key: 0 for key in range(0, 10)}
    # print(dict_size)
    for root, dirs, files in os.walk(directory):
        for file in files:
            size = os.stat(os.path.join(root, file))[6]
            for key in dict_size.keys():
                if size <= key:
                    dict_size[key] = dict_size[key] + 1
                    break
                elif size > 1000000000:
                    print('Есть файлы больше 1 миллиарда байт (1гб)')
    return dict_size


print(stat_dir(os.getcwd()))

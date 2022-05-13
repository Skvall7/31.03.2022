import os
import json


def stat_dir(directory):
    dict_size = {10 ** key: (0, []) for key in range(0, 10)}
    for root, dirs, files in os.walk(directory):
        for file in files:
            size = os.stat(os.path.join(root, file))[6]
            for key in dict_size.keys():
                if size <= key:
                    fs = file.split('.')[1]
                    # dict_size[key][1].extend(fs)
                    # es = ''.join(dict_size[key][1])
                    dict_size[key] = dict_size[key][0] + 1, list(set([*dict_size[key][1], fs]))
                    break
                elif size > 1000000000:
                    print('Есть файлы больше 1 миллиарда байт (1гб)')
    return dict_size


print(stat_dir(os.getcwd()))
with open('data.json', 'w') as f:
    json.dump(stat_dir(os.getcwd()), f)

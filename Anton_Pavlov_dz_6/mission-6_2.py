from pprint import pprint
from collections import Counter


def get_parse_attrs(line_pars: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    line_pars = line_pars.split(' ')
    return line_pars[0], line_pars[5].strip('"'), line_pars[6]


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    line = fr.readline()
    while line:
        list_out += [get_parse_attrs(line)]
        line = fr.readline()

count_list = [count[0] for count in list_out]
max_count = Counter(count_list).most_common(5)
pprint(max_count)

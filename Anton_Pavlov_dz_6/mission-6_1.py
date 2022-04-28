from pprint import pprint


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

pprint(list_out)

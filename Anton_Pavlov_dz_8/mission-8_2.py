import re


def parse(line_raw: str):
    RE_LINE = re.compile(r'(.+\b)\W{6}(.+\b).{3}(\w+)\s+(.+\b)\s.{10}(\d+)\s(\d+)')
    print(RE_LINE.findall(line_raw))
    assert RE_LINE.match(line_raw), f'wrong line: {line_raw}'


if __name__ == '__main__':
    with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
        for line in fr:
            parse(line)

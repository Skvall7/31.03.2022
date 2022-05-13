import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'^(\w+\b@)(\w+\b\.)[a-z]{2}$')
    assert RE_MAIL.match(email), f'wrong email: {email}'
    mail = {'username': email.split('@')[0], 'domain': email.split('@')[1]}
    return print(mail)


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')

price_tags = [58.99, 66.1, 15.15, 48.09, 100, 24.2, 23.59, 22.9, 23.45, 67.00]
print(id(price_tags))
top = []
price_tags_sort = sorted(price_tags, reverse=True)
for price_tag in sorted(price_tags):
    price_rub = int(price_tag) // 1
    price_kop = int(price_tag * 100 % 100)
    if 0 <= price_kop < 10:
        price_kop = f'0{price_kop}'
    print(f'{price_rub} руб. {price_kop} коп.', end=', ')
print(id(price_tags))
for price_tag in price_tags_sort:
    price_rub = int(price_tag) // 1
    price_kop = int(price_tag * 100 % 100)
    if 0 <= price_kop < 10:
        price_kop = f'0{price_kop}'
    print(f'{price_rub} руб. {price_kop} коп.', end=', ')
print()
for price_tag in price_tags_sort[:5]:
    price_rub = int(price_tag) // 1
    price_kop = int(price_tag * 100 % 100)
    if 0 <= price_kop < 10:
        price_kop = f'0{price_kop}'
    print(f'{price_rub} руб. {price_kop} коп.', end=', ')

def get_uniq_numbers(src: list):
    result = [number for number in src if src.count(number) == 1]
    # for n in src:
    #     if not src.count(n) <= 1:
    #         while src.count(n) != 0:
    #             src.remove(n)
    return result


source = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(source))

def get_numbers(src: list):
    generator = (numbers for numbers in range(0, len(src) + 1))
    result = [number for number in src if number > src[next(generator) - 1]]
    if src[0] > src[-1]:
        result.pop(0)
    return result


source = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(source))

max_num = int(input())
generator = (numbers for numbers in range(1, max_num + 1, 2))
print(next(generator))
print(next(generator), next(generator))

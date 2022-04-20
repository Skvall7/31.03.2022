def num_gen(num):
    for number in range(1, num + 1, 2):
        yield number


generic = num_gen(15)
# print(next(generic), next(generic))
print(next(generic))

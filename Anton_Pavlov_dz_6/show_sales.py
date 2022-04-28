def sales(argv):
    with open('bakery.csv', 'r', encoding='utf-8') as fr:
        i = 0
        start = int(argv[1])
        if len(argv) < 3:
            end = 0
        else:
            end = int(argv[2])
        for line in fr:
            i += 1
            if start <= i:
                print(*line.split())
                if end == i:
                    return
        return


if __name__ == '__main__':
    import sys
    exit(sales(sys.argv))

def sales(argv):
    with open('bakery.csv', 'r+', encoding='utf-8') as fr:
        i = 0
        start = int(argv[1])
        sale = argv[2]
        while i <= 0:
            i += 1
            if start == i:
                cursor = fr.tell()
                fr.seek(cursor)
                fr.writelines(sale)
                return
            fr.readline()
        return


if __name__ == '__main__':
    import sys
    exit(sales(sys.argv))

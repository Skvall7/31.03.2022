def sales(argv):
    with open('bakery.csv', 'a', encoding='utf-8') as fa:
        fa.write(f'{argv[1]}\n')
        return


if __name__ == '__main__':
    import sys
    exit(sales(sys.argv))

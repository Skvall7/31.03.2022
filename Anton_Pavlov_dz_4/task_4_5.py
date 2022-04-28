from utils import currency_rates_adv


def c_r(argv):
    code = argv[1]
    return currency_rates_adv(code)


if __name__ == '__main__':
    import sys
    exit(c_r(sys.argv))

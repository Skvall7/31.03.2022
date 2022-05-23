class Number:

    def __init__(self):
        return

    @staticmethod
    def list():
        num = []
        while True:
            try:
                x = input('Ведите число: ')
                if x == 'stop':
                    break
                num.append(int(x))
            except:
                continue
        return f'{num}'


print(Number.list())

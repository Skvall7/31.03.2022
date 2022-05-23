class Data:

    @classmethod
    def in_int(cls, data: str):
        data = data.split('.')
        number = [int(num) for num in data]
        print(*number)

    @staticmethod
    def valid(data: str):
        data = data.split('.')
        number = [int(num) for num in data]
        if number[0] < 1 or number[0] > 31:
            print('Неверный формат даты')
        if number[1] < 1 or number[1] > 12:
            print('Неверный формат даты')


Data.in_int('23.12.1985')
Data.valid('31.13.1985')

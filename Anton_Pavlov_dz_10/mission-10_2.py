class Clothes:
    def __init__(self):

        pass


class Coat(Clothes):
    def __init__(self, size: float):
        super().__init__()
        self.size = size

    @property
    def calculate(self):
        calc = (self.size / 6.5 + 0.5) * 100 // 1 / 100
        return calc


class Costume(Clothes):
    def __init__(self, height: int):
        super().__init__()
        self.height = height

    @property
    def calculate(self):
        calc = (2 * self.height + 0.3) * 100 // 1 / 100
        return calc


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3

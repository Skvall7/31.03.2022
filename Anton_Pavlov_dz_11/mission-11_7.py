class Complex:

    def __init__(self, a: int, b=0):
        self.a = a
        self.b = b

    def __int__(self):
        i = -1
        c = self.a + self.b * i
        return c

    def __add__(self, other):
        i = -1
        f = (self.a + self.b * i) + (int(other))
        return f

    def __mul__(self, other):
        i = -1
        f = (self.a + self.b * i) * (int(other))
        return f

    def __truediv__(self, other):
        i = -1
        f = (self.a + self.b * i) / (int(other))
        return int(f)


x = Complex(7, 2)
y = Complex(9, 4)
print(x.__int__(), y.__int__())
print(Complex(x + y).__int__())
print(Complex(x * y).__int__())
print(Complex(x / y).__int__())

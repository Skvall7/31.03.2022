class Division:

    def __init__(self, param_1):
        self.param_1 = param_1

    def div(self, param_2):
        try:
            result = self.param_1 / param_2
            return result
        except:
            return f'Деление на ноль недопустимо'


d = Division(1)
print(d.div(0))

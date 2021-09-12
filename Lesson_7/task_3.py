class Cell:
    def __init__(self, lenth):
        self.lenth = lenth

    def __add__(self, other):
        return Cell(self.lenth + other.lenth)

    def __sub__(self, other):
        res = Cell(self.lenth - other.lenth)
        return res if self.lenth > other.lenth else 'Первая клетка короче второй! Разность невозможна!'

    def __mul__(self, other):
        return Cell(self.lenth * other.lenth)

    def __floordiv__(self, other):
        return Cell(self.lenth // other.lenth)

    def make_order(self, lines):
        return '\n'.join(['*' * lines for i in range(self.lenth // lines)]) + '\n' + '*' * (self.lenth % lines)

    def __str__(self):
        return '*' * self.lenth


a = Cell(15)
b = Cell(4)
print('Первая клетка\n', a)
print('Вторая клетка\n', b)
print('Сумма\n', a + b)
print('Разность\n', a - b)
print('Умножение\n', a * b)
print('Деление\n', a // b)
print('Разбивка на ряды\n', a.make_order(4))

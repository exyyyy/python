class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


worker_1 = Position('Alexey', 'Mikheev', 'ingeneer', 10000, 2000)

print(f'Сотрудник: {worker_1.get_full_name()}\nДоход сотрудника: {worker_1.get_total_income()} у.е.')

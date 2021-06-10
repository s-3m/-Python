class Worker:
    def __init__(self, name, surname, position, _income):
        money = {'wage': 20000, 'bonus': 30000}
        self.name = name
        self.surname = surname
        self.position = position
        self.income = money


class Position(Worker):
    def get_full_name(self):
        full_name = self.surname + ' ' + self.name
        print(full_name)

    def get_total_income(self):
        total_income = self.income['wage'] + self.income['bonus']
        print(total_income)


first_worker = Position('Иван', 'Батарекйкин', 'юрист', 3000)
first_worker.get_full_name()
first_worker.get_total_income()
print(first_worker.income)
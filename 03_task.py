class Worker:

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": profit, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{sum(self._income.values())}"


info = Position('Ivan', 'Ivanov', 'accountant', 40000, 15000)
print(info.get_full_name(), info.get_total_income())

info = Position('Petr', 'Petrov', 'security', 60000, 5000)
print(info.get_full_name(), info.get_total_income())
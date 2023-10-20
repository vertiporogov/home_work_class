class Employee:
    """Класс для представления сотрудника"""
    raise_coef = 1.04

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.pay + other.pay
        return None

    def raise_pay(self):
        self.pay *= self.raise_coef


class Developer(Employee):
    raise_coef = 1.1

    def __init__(self, name, surname, pay, prog_lang):
        super().__init__(name, surname, pay)
        self.prog_lang = prog_lang


emp1 = Employee('Test', 'Testov', 50000)

dev1 = Developer('Ivan', 'Ivanov', 100000, 'python')

total_pay = emp1 + dev1
print(total_pay)

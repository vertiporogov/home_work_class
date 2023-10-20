

class Employee:
    """Класс для представления сотрудника"""
    raise_coef = 1.5

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.__pay = pay

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.surname}, {self.pay})'

    def __str__(self):
        return f'{self.fullname} ({self.pay})'

    def __len__(self):
        return len(self.fullname)

    def __add__(self, other):
        return self.pay + other.pay

    def raise_pay(self):
        self.__pay *= self.raise_coef

    @property
    def email(self):
        return f'{self.name.lower()}.{self.surname.lower()}@myjobmail.com'

    @property
    def pay(self):
        return self.__pay

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

    @fullname.setter
    def fullname(self, data_string):
        name, surname = data_string.split(' ')
        self.name = name
        self.surname = surname


if __name__ == '__main__':
    emp_1 = Employee('Ivan', 'Ivanov', 60000)
    emp_2 = Employee('Petr', 'Petrov', 100000)
    # print(repr(emp_1))
    # result = emp_1 + emp_2
    #
    # print(result)

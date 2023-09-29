import datetime


class Employee:
    '''Класс для представления сотрудника'''

    raise_coef = 1.5
    def __init__(self, name, surname, pay):
        self.name = name
        self.surname =surname
        self.__pay = pay

    def raise_pay(self):
        self.__pay *= self.raise_coef

    @classmethod
    def from_string(cls, data_string):
        name, surname, pay = data_string.split(' ')
        pay = int(pay)

        return cls(name, surname, pay)
    @classmethod
    def set_raise_amount(cls, new_coef):
        cls.raise_coef = new_coef

    @staticmethod
    def is_workday():
        now = datetime.datetime.now().replace(day=30)
        if now.weekday() == 5 or now.weekday() == 6:
            return False
        return True

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

    # TestCase#1 email
    assert emp_1.email == 'ivan.ivanov@myjobmail.com'

    # TestCase#1.1
    emp_1.name = 'Semen'
    assert emp_1.email == 'semen.ivanov@myjobmail.com'

    # TestCase#2 RaisePay
    emp_1.raise_pay()
    assert 60000 * Employee.raise_coef == emp_1.pay
    assert emp_1.pay == 90000

    # TestCase#3 New Object
    emp_2 = Employee.from_string('Petr Petrov 70000')
    assert isinstance(emp_2, Employee)
    assert emp_2.name == 'Petr'
    assert emp_2.surname == 'Petrov'
    assert emp_2.pay == 70000

    # TestCase#4 Set Raise Amount
    Employee.set_raise_amount(2)
    assert Employee.raise_coef == 2
    assert emp_1.raise_coef == 2
    assert emp_2.raise_coef == 2

    # TestCase#5 Is Work Day
    assert Employee.is_workday() == False

    # TestCase#6 Fullname
    assert emp_1.fullname == 'Semen Ivanov'
    assert emp_2.fullname == 'Petr Petrov'

    # TestCase#7 Set Fulname (name, surname)
    emp_1.fullname = 'Ivan Ivanov'
    assert emp_1.name == 'Ivan'
    assert emp_1.surname == 'Ivanov'

    # emp5 = Employee('alex', 'vert', 200000)
    # print(emp5.pay)
    # emp5.set_raise_amount(5)
    # emp5.raise_pay()
    # print(emp5.pay)

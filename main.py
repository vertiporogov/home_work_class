
class Employee:
    '''Класс для представления сотрудника'''

    raise_coef = 1.5

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname =surname
        self.email = f'{self.name.lower()}.{self.surname.lower()}@mail.com'
        self.pay = pay

    def raise_pay(self):
        self.pay *= self.raise_coef

if __name__ == '__main__':
    emp_1 = Employee('Ivan', 'Ivanov', 60000)

    #TestCase #1 email
    assert emp_1.email == 'ivan.ivanov@mail.com'

    #TestCase #2 RaisePay
    emp_1.raise_pay()
    assert 60000 * Employee.raise_coef == emp_1.pay

    assert emp_1.pay == 90000

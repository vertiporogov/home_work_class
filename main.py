
if __name__ == '__main__':
    class Employee:
        '''Класс для представления сотрудника'''

        # raise_amount = 1.04
        nummer_of_employee = 0

        def __init__(self, name, surname, pay):
            self.name = name
            self.surname =surname
            self.email = f'{self.name}.{name}@mail.com'
            self.pay = pay

            Employee.nummer_of_employee += 1

        def full_name(self):
            return f'{self.name} {self.surname}'

        def apply_raise(self):
            self.pay = int(self.pay * self.raise_amount)

            return self.pay


    # Employee.raise_amount = 2.2
    # emp_1.raise_amount = 1.08

    emp_1 = Employee('Ivan', 'Ivanov', 60000)
    emp_2 = Employee('Petr', 'Petrov', 50000)
    # emp_1.raise_amount = 2



    # print (emp_1)
    # print (emp_1.name)
    # print (emp_1.surname)
    # print (emp_1.pay)
    # print (emp_1.email)
    # print(emp_1.apply_raise())

    print(Employee.nummer_of_employee)

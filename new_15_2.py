from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name, surname, pay):
        print('Добавлен сотрудник')
        self.name = name
        self.surname = surname
        self.pay = pay
        # super().__init__()


class MixinLog:

    ID = 0

    def __init__(self,name, surname, pay):
        super().__init__(name, surname, pay)
        MixinLog.ID += 1
        print(f'Добавлен сотрудник с номером {self.ID}')


class Developer(MixinLog, Employee):

    def __init__(self, name, surname, pay, prog_lang):
        print('Добавлен разработчик')
        super().__init__(name, surname, pay)
        self.prog_lang = prog_lang


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_set_del(self):
        self.x += 1
        self.y = 100
        del self.y

class PointSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_set_del(self):
        self.x += 1
        self.y = 100
        del self.y


p = Point(1,2)

ps = PointSlots(3,4)

import timeit

t1 = timeit.timeit(p.get_set_del)
t2 = timeit.timeit(ps.get_set_del)

print(t1)
print(t2)




# dev = Developer('ivan', 'ivanov', 100000, 'python')
# dev = Developer('ivan', 'ivanov', 100000, 'python')
# dev = Developer('ivan', 'ivanov', 100000, 'python')
# print(dev.__dict__)
# print(Developer.__mro__)

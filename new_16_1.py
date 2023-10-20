class ShellExeption(Exception):
    pass


class ShebanShellException(Exception):

    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.messag = args[0]
        else:
            self.messag = 'Должен быть шебанг'


class EmptyShellException(Exception):

    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.messag = args[0]
        else:
            self.messag = 'Файл не может быть пустым'


class ShellExecutor:

    def __init__(self, file_content):
        self.file_content = file_content
        if len(self.file_content) == 0:
            raise EmptyShellException

        if self.file_content[0] != '#':
            raise ShebanShellException('не хватает шебанг')


content = '#!/bin/bahs'  # правильно
# content = '!/bin/bahs'  # не хватает шебанг
# content = ''  # пустой скрипт

try:
    shell_executor = ShellExecutor(content)
except EmptyShellException as ex:
    print(ex.messag)
except ShebanShellException as ex:
    print(ex.messag)
else:
    print('Все прошло хорошо')






# class TryExec:
#
#
#     def func1(self):
#         self.func2()
#         print('Штатная работа метода func1')
#
#     def func2(self):
#         self.func3()
#         print('Штатная работа метода func2')
#
#     def func3(self):
#         try:
#             100 / 0
#         except ZeroDivisionError:
#             print('Возникновение ошибки в func3')
#         print('Штатная работа метода func3')


# come_obj = TryExec()
# come_obj.func1()



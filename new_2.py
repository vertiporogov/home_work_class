class EvenRange:

    def __init__(self, max_num):
        self.__max_num = max_num
        self.__step = 2
        self.__start = 0


    def __iter__(self):
        self.current_value = self.__start - self.__step
        return self

    def __next__(self):
        self.current_value += self.__step

        if self.current_value < self.__max_num:
            return self.current_value

        raise StopIteration



it = iter(EvenRange(10))

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# for i in EvenRange(10):
#     print(i)

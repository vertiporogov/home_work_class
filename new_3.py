class MyOpen:

    def __init__(self, filename, mode):
        self.__filename = filename
        self.__mode = mode

    def __enter__(self):
        self.__fp = open(self.__filename, self.__mode)
        return self.__fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__fp.close()


with MyOpen('hello.txt', 'r') as fp:
    print(fp.read())

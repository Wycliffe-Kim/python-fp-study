from typing import Callable


class Calculator:
    def __init__(self, input: int | float = 0):
        self.__data = input

    def add(self, value: int | float):
        return Calculator(self.__data + value)

    def sub(self, value: int | float):
        return Calculator(self.__data - value)

    def mul(self, value: int | float):
        return Calculator(self.__data * value)

    def div(self, value: int | float):
        return Calculator(self.__data / value)

    def map(self, f: Callable[[int | float], int | float]):
        return f(self.__data)

    def chain(self, f: Callable[[int | float], int | float]):
        f(self.__data)
        return Calculator(self.__data)


def log(title: str):
    def log_inner(data):
        print(f'{title}: {data}')

    return log_inner


print_add_result = log('add result')
print_sub_result = log('sub result')
print_mul_result = log('mul_result')
print_total_result = log('result is')


def main():
    (Calculator()
     .add(2)
     .chain(print_add_result)
     .add(3)
     .chain(print_add_result)
     .add(4)
     .chain(print_add_result)
     .add(5)
     .chain(print_add_result)
     .sub(9)
     .chain(print_sub_result)
     .mul(2)
     .chain(print_mul_result)
     .div(5)
     .chain(print_total_result))

from functools import reduce
from typing import Callable


def make_add_function(a: int):
    def add_with(b: int):
        return a + b

    return add_with


def make_add_function_with_additional_op(a: int, additional_op: Callable[[], int]):
    def add_with_val_and_op(b: int):
        return a + b + additional_op()

    return add_with_val_and_op


def main():
    add_with_1 = make_add_function(1)
    print('add_with_1:', add_with_1(2))

    add_with_val_and_op = make_add_function_with_additional_op(
        1, lambda: reduce(lambda a, b: a + b, range(5), 0))

    print('add_with_val_and_op:', add_with_val_and_op(2))

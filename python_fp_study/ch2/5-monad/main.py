from typing import Callable, TypeVar, Generic

T = TypeVar('T')


class Monad(Generic[T]):
    @staticmethod
    def of(value: T):
        return Monad[T](value)

    def __init__(self, value: T):
        self.__data = value

    def map(self, f: Callable[[T], T]):
        return Monad[T](f(self.__data))

    def done(self, f: Callable[[T], T]):
        return f(self.__data)


def identity(data: T):
    return data


def twice(data: T):
    return data * 2


def log(title: str):
    def log_inner(data):
        print(f'{title}: {data}')
        return data

    return log_inner


def main():
    operation = (Monad[int].of(1)  # Monad(1)
                 .map(log('first phase'))
                 .map(lambda d: d + 2)  # Monad(1 + 2)
                 .map(log('second phase'))
                 .map(lambda d: d * 2)   # Monad(3 * 2)
                 .map(log('last phase')))

    print('monad chain done with identity:', operation.done(identity))  # 6
    print('monad chain done with twice:', operation.done(twice))  # 12

from functools import reduce


def sum(total: float, current: float):
    return total + current


def total(arr: list[float]):
    return reduce(sum, arr, 0)


def size(arr: list[float]):
    return len(arr)


def divide(a: float, b: float):
    return a / b


def average(arr: list[int]):
    return divide(total(arr), size(arr))


def main():
    print('referential transparent! Average is always', average([80, 90, 100]))

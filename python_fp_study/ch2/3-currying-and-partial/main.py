import pydash as _


def add4(a: int, b: int, c: int, d: int):
    return a + b + c + d


def main():
    add_with_partial = _.partial(add4, 1)
    print('partial:', add_with_partial(2, 3, 4))

    add_with_curry = _.curry(add4)
    add4_with_1 = add_with_curry(1)
    print('add4_with_1:', add4_with_1(2, 3, 4))
    add4_with_1_and_2 = add_with_curry(1, 2)
    print('add4_with_1_and_2', add4_with_1_and_2(3, 4))

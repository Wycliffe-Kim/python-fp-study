import toolz as tz
import pydash as _


def add_for_curry(value: int, data: list[int]):
    return _.map_(data, lambda d: d + value)


def mul_for_curry(value: int, data: list[int]):
    return _.map_(data, lambda d: d * value)


add = _.curry(add_for_curry)
mul = _.curry(mul_for_curry)


def main():
    calc = tz.compose(mul(2), add(10))
    print('[0, 1, 2, 3, 4] + 10 * 10; compose with each element:', calc(range(5)))

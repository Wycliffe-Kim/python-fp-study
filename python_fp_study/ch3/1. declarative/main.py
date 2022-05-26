from functions.map import map
from functions.filter import filter
from functions.reduce import reduce


def run_map():
    print('----- run_map -----')

    arr = list(range(10))

    def proc(data: int):
        return data * 2

    print('before:', arr)
    arr = map(arr, proc)
    print('after:', arr)


def run_filter():
    print('----- run_filter -----')

    arr = list(range(10))

    def proc(data: int):
        return data > 5

    print('before:', arr)
    arr = filter(arr, proc)
    print('after:', arr)


def run_reduce():
    print('----- run_reduce -----')

    arr = list(range(10))

    def proc(acc, data):
        return acc + data

    print('before:', arr)
    print('after:', reduce(arr, proc))


def calc_variance():
    print('----- calc_variance -----')

    arr = list(range(10))

    def sum(acc: int, data: int):
        return acc + data

    def total(arr: list[int]):
        return reduce(arr, sum)

    def size(arr: list[int]):
        return len(arr)

    def average(arr: list[int]):
        return total(arr) / size(arr)

    def map_proc(arr: list[int]):
        avg = average(arr)

        def map_proc_inner(data: int):
            return pow(data - avg, 2)

        return map_proc_inner

    numerator_inner = map(arr, map_proc(arr))

    numerator = reduce(numerator_inner, sum, 0)
    denominator = size(arr)

    print('before:', arr)
    variance = numerator / denominator
    print('after:', variance)


jobs = [run_map, run_filter, run_reduce, calc_variance]
map(jobs, lambda job: job())

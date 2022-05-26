from inspect import signature
from typing import Callable, List, Optional, TypeVar

T = TypeVar('T')


def reduce(arr: List[T], fn: Callable[[T, T, Optional[int], Optional[List[T]]], T], accumulator: T | None = None):
    length = len(arr)
    sig = signature(fn)
    len_param = len(sig.parameters)

    idx = 0
    if accumulator == None and length > 0:
        accumulator = arr[idx]

    if len_param == 4:
        def f(): return fn(accumulator, arr[idx], idx, arr)
    elif len_param == 3:
        def f(): return fn(accumulator, arr[idx], idx)
    else:
        def f(): return fn(accumulator, arr[idx])

    while idx < length:
        accumulator = f()
        idx += 1

    return accumulator

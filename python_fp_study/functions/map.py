from typing import Callable, List, TypeVar, Optional
from inspect import signature

T = TypeVar('T')


def map(arr: List[T], fn: Callable[[Optional[T], Optional[int], Optional[List[T]]], List[T]]):
    length = len(arr)
    result: List[T] = [None] * length
    sig = signature(fn)
    len_param = len(sig.parameters)
    if len_param == 3:
        def f(): return fn(arr[idx], idx, arr)
    elif len_param == 2:
        def f(): return fn(arr[idx], idx)
    elif len_param == 1:
        def f(): return fn(arr[idx])
    else:
        f = fn

    for idx in range(length):
        result[idx] = f()

    return result

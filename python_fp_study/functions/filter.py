from typing import Callable, List, TypeVar, Optional
from inspect import signature

T = TypeVar('T')


def filter(arr: List[T], predicate: Callable[[Optional[T], Optional[int]], T]):
    length = len(arr)
    result: List[T] = []
    sig = signature(predicate)
    len_param = len(sig.parameters)
    if len_param == 2:
        def f(): return predicate(value, idx)
    elif len_param == 1:
        def f(): return predicate(value)
    else:
        f = predicate

    idx = 0
    while idx < length:
        value = arr[idx]
        if f() == True:
            result.append(value)

        idx += 1

    return result

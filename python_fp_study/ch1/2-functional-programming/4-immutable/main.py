from copy import deepcopy


def main():
    obj = {
        "test1": 1,
        "test2": "2",
        "test3": {
            "test3-1": 3,
            "test3-2": "4"
        }
    }

    obj_copied = deepcopy(obj)
    obj_copied["test3"]["test3-1"] = 100

    print('obj copy before:', obj)
    print('obj copy after:', obj_copied)

    arr = list(range(10))
    arr_copied = deepcopy(arr)
    arr_copied[9] = 100

    print('arr copy before:', arr)
    print('arr copy after:', arr_copied)

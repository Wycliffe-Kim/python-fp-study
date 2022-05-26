from ....functions.map import map


def imperative_case():
    print('----- imperative_case -----')
    array = list(range(10))
    print('before:', array)

    for i in array:
        array[i] = array[i] ** 2
    print('after:', array)


def declarative_case():
    print('----- declarative_case -----')
    array = list(range(10))
    print('before:', array)

    array = map(array, lambda x: x ** 2)
    print('after:', array)


def main():
    imperative_case()
    declarative_case()

global count
count = 0


def not_pure():
    global count
    count += 1
    return count


def pure(count):
    count += 1
    return count


def main():
    global count
    print('before not_pure:', count)
    count = not_pure()
    print('after not_pure:', count)

    print('before pure:', count)
    count = pure(count)
    print('after pure:', count)

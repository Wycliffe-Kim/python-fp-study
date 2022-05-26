global count
count = 0


def not_referential_transparent():
    global count
    count += 1
    return count


def referential_transparent(count):
    count += 1
    return count


def main():
    global count
    print('before not_referential_transparent:', count)
    count = not_referential_transparent()
    print('after not_referential_transparent:', count)

    print('before referential_transparent:', count)
    count = referential_transparent(count)
    print('after referential_transparent:', count)

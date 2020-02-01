def lexi(st):
    i, j = 0, len(st) - 1
    while i + 1 <= j:

        if st[i] > st[i + 1]:
            st = st[:i] + st[i + 1:]
            break
        i += 1
    return st


print(lexi('abczd'))
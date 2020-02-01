def perm_of_length_k(n, k):
    perm = [[]]
    res = []

    perm_length = len(perm)
    s = 0
    while s < perm_length:
        each = perm[s]
        for i in range(1, n + 1):
            l = list(each)
            l.append(i)
            if len(l) < k:
                perm.append(l)
            elif len(l) == k:
                res.append(l)
        print(perm)
        s += 1
        perm_length = len(perm)
        print('\n')


    print('\n\n\n\n')
    print(res)


def perm_of_length_k2(n, k):
    perms = [[]]
    res =  []
    for i in range(1, n):
        new_perms = []
        for perm in perms:
            for j in range(len(perm) + 1):
                new_perms.append(perm[:j] + [i] + perm[j:])  ###insert n
                if len(new_perms) == k:
                    res.append(new_perms)
                    new_perms = []

            print("\n")
        perms = new_perms
        print(perms)
        print("\n\n\n")

    print("\n\n\n")
    return res

print(perm_of_length_k(4, 3))
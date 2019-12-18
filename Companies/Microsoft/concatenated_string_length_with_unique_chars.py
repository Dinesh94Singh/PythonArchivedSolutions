import collections
def concat(arr):
    m = collections.defaultdict(list)
    for i, st in enumerate(arr):
        if len(set(st)) != len(st):
            continue
        m[len(st)].append(i)
    lst = []
    for size in sorted(m, reverse=True):
        lst += m[size]
    res = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            idx1, idx2 = lst[i], lst[j]
            if not (set(arr[idx1]) & set(arr[idx2])):
                return len(arr[idx1]) + len(arr[idx2])
    return 0
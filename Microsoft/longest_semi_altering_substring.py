def solution(st):
    start, i, j = 0, 0, len(st)
    res = temp = 0
    while i + 2 < j:
        view = st[i:i + 3]
        if view == 'aaa' or view == 'bbb':
            i += 1
            temp = i + 1 - start
            start = i + 1
            res = max(temp, res)
        i += 1
    if res == 0:
        res = len(st)
    return res


print(solution('abaaaaa'))
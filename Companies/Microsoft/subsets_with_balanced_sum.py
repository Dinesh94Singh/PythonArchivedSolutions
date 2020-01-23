import heapq


def subset(arr, n):
    heap = [(0, i) for i in range(n)]
    res = [[] for _ in range(n)]

    for each in sorted(arr, reverse=True):
        val, idx = heapq.heappop(heap)
        total = val + each
        res[idx].append(each)

        heapq.heappush(heap, (total, idx))

    return res


ip = [1, 2, 3, 4, 5, 2, 2, 3, 9]
total_subsets = 3
print(subset(ip, total_subsets))

# Time Complexity should be O(n):
# from above method, which is O(n) + klog(k), since the maximum of k is 26, so the actual time complexity is O(n).

from collections import Counter
import heapq

def min_del(string):
    counts = Counter(Counter(string).values())
    queue = []
    for ch_cnt, freq in counts.items():
        heapq.heappush(queue, (-ch_cnt, freq))
    ans = 0
    while queue and queue[0][0] != 0:
        ch_cnt, freq = heapq.heappop(queue)
        if freq > 1:
            ans += freq - 1
            if queue and queue[0][0] == ch_cnt + 1:
                next_cnt, next_freq = heapq.heappop(queue)
                next_freq += freq - 1
            else:
                next_cnt = ch_cnt + 1
                next_freq = freq - 1
            heapq.heappush(queue, (next_cnt, next_freq))
    return ans
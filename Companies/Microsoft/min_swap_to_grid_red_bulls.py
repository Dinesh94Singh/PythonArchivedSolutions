"""
Find the minimum number of swaps requied to
S = WRRWWR
Output - 1.WRRWRW 2.WRRRWW
"""


def min_num_swap(s):
    red_indices = []
    for i in range(len(s)):
        if s[i] == 'R':
            red_indices.append(i)
    min_swaps = 0
    mid = len(red_indices) // 2
    for i in range(len(red_indices)):
        # number of swaps for each R is the distance to mid, minus the number of R's between them
        min_swaps += abs(red_indices[mid] - red_indices[i]) - abs(mid - i)
    return min_swaps


print(min_num_swap('WRRWRW'))
print(min_num_swap('WRWRWR'))
print(min_num_swap('RRRWRR'))
print(min_num_swap('WRWWWRWWWR'))

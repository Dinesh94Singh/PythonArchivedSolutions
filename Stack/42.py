"""

42. Tripping rain water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water
(blue section) are being trapped. Thanks Marcos for contributing this image! (Refer leet code for the image)

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

"""


def trap_my_brute_force(height):
    """
    This fails for the input [4, 2, 3]
    """
    res = 0
    if len(height) == 0:
        return 0
    i = 0
    while i < (len(height)):
        if height[i] == 0:
            i += 1
            continue
        left_bound = height[i]
        right_bound = None
        for j in range(i+1, len(height)):
            if height[j] >= height[i]:
                right_bound = height[j]
                break
        if j == len(height) - 1 and not right_bound:
            i += 1
            continue
        if i + 1 == j:
            # if there are no elements between i and j then continue
            i = j
        else:
            minimum = min(left_bound, right_bound)
            total = 0

            for k in range(i+1, j):
                total += minimum - height[k]
            print('total is ', total)
            if i <= j:
                i = j
            res += total
    return res

# print(trap_my_brute_force([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(trap_my_brute_force([2, 0, 2]))
# print(trap_my_brute_force([4, 2, 3]))


def trap_brute_force(height):
    """
    Time Limit exceeds for this - O(n^2)
    """
    if len(height) <= 1:
        return 0
    res = 0
    for idx, each in enumerate(height):
        left_bound, right_bound = each, each
        i, j = idx, idx
        while i >= 0:
            left_bound = max(left_bound, height[i])
            i -= 1
        while j <= len(height) - 1:
            right_bound = max(right_bound, height[j])
            j += 1
        minimum = min(left_bound, right_bound)
        print('left bound is', left_bound, 'right bound is', right_bound, 'min is', min(left_bound, right_bound))
        res += (minimum - each)
    return res

print(trap_brute_force([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap_brute_force([2, 0, 2]))
print(trap_brute_force([4, 2, 3]))
print(trap_brute_force([]))
print(trap_brute_force([4]))

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


def trap(height):
    res, size = 0, len(height)
    left_max, right_max = [0] * size, [0] * size
    left_max[0], right_max[-1] = height[0], height[-1]
    for i in range(1, size):
        left_max[i] = max(left_max[i - 1], height[i])
    for i in range(size - 2, 0, -1):
        right_max[i] = max(right_max[i + 1], height[i])
    for i in range(1, size - 1):
        res += min(right_max[i], left_max[i]) - height[i]
    return res


trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

'''

11. Container with most water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

Solution:

1. Find the first and second max numbers
2. Count the total number of numbers in between the first and second max index
3. Output = second_max * total_numbers

Leetcode Solution:
1. Two pointers, and cal max. Each pointer at the extreme ends and find the max.

'''

def maxArea(height):
  first = max_area = 0
  last = len(height) - 1
  while first < last:
    minimum = min(height[first], height[last])
    max_area = max(max_area, (last - first) * minimum)
    print('max area is', max_area)
    if height[first] < height[last]:
      first += 1
    else:
      last -= 1
  return max_area    

height = []
maxArea(height)
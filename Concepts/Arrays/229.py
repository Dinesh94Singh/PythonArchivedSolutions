'''
229. Majority Element 2

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]

Solution:

 - Boyer Moore voting problem

 Majority Element 1 - #169
 
 def majorityElement(nums):
  count = 0
  candidate = None

  for num in nums:
    print('current num is ', num)
    if count == 0:
      candidate = num
    count += (1 if num == candidate else -1)

  return candidate

Intution - In the given problem the number is said to be majority element, if it occurs more than n/3 times

since its n/3 - atmost only 2 numbers should be the majority elemnts => eg: n = 12 => 10/3 = 4

2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4 => at most only 2 are possible.

Soltion: Just like #169 keep track of 2 candidates
'''

def majorityElement(nums):
  candidate1, candidate2 = 0, 0
  count1, count2 = 0, 0
  res = []
  for num in nums:
    if candidate1 == num:
      count1 += 1
    elif candidate2 == num:
      count2 += 1
    elif count1 == 0:
      candidate1 = num
      count1 += 1
    elif count2 == 0:
      candidate2 = num
      count2 += 1
    else:
      count1 -= 1
      count2 -= 1
  c1 = c2 = 0
  print('candidate1 ', candidate1)
  print('candidate2 ', candidate2)
  for num in nums:
    if num == candidate1:
      c1 += 1
    if num == candidate2:
      c2 += 1
  print(c1, c2) 
  if c1 > len(nums)/3:
    res.append(candidate1)
  if c2 > len(nums)/3:
    res.append(candidate2)
  return res

majorityElement([3, 2, 3])
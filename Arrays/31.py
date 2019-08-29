'''

31. Next Permutation 
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2 -> 2, 1, 3 -> 2, 3, 1 -> 3, 1, 2 -> 3, 2, 1
3,2,1 → 1,2,3 # can't have more than this, so sorted ascending order
1,1,5 → 1,5,1
'''

# def nextPermutation(self, nums: List[int]) -> None:

'''
Brute Force => All possible permutations and find the next largest one among those. O(n!)

Though Process.
1. We are keeping the left most digits constant and trying to re-arrange between the others. => to rearrange we need atleast 2 numbers at the end.

1. First, find the decreasing element from the right most side.
2. Second, find the element larger than the element found at step 1 in between the path of len(nums) till the position of element from step1
3. Reverse from the position of element from step1 + 1 till end
'''

def reverse(nums, start):
  i = start
  j = len(nums) - 1
  while i < j:
    nums[j], nums[i] = nums[i], nums[j]
    i += 1
    j -= 1
  print(nums)

reverse([1, 2, 3, 4], 0)
reverse([1, 2, 3, 4], 2)

def nextPermutation(nums):
  i = len(nums) - 2
  while i >= 0 and nums[i+1] <= nums[i]:
    i = i-1
  if (i >= 0):
    # not in decreasing order - if this is the case, reverse it
    j = len(nums) - 1
    while j >= 0 and nums[j] <= nums[i]:
      j = j-1
    nums[i], nums[j] = nums[j], nums[i]
  reverse(nums, i+1)

nextPermutation([1, 2, 3, 4]) # output should be 1, 2, 4, 3
nextPermutation([1, 5, 1])
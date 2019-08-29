'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''

# def removeDuplicates(self, nums: List[int]) -> int:

'''
2 pointer technique where 1 pointer stays at the duplicate element and the other pointer goes on till its find non-duplicate element.

Once the non-duplicate element is found, replace that with the index where duplicate element is present

eg - 1, 1, 3, 3, 3, 3, 5, 7, 8, 9



removeDuplicates1([1, 1, 3, 3, 3, 3, 5, 7, 8, 9])...
[1, 1, 3, 3, 3, 3, 5, 7, 8, 9] searching for something other than 1
[1, 3, 3, 3, 3, 3, 5, 7, 8, 9]
[1, 3, 3, 3, 3, 3, 5, 7, 8, 9] searching for something other than 3
[1, 3, 3, 3, 3, 3, 5, 7, 8, 9] searching for something other than 3
[1, 3, 3, 3, 3, 3, 5, 7, 8, 9] searching for something other than 3 - found 5
[1, 3, 5, 3, 3, 3, 5, 7, 8, 9] replace the duplicate 3 pointed by i with 5
[1, 3, 5, 7, 3, 3, 5, 7, 8, 9] replace the duplicate 3 pointed by i with 7
[1, 3, 5, 7, 8, 3, 5, 7, 8, 9] replace the duplicate 3 pointed by i with 8
[1, 3, 5, 7, 8, 9, 5, 7, 8, 9] replace the duplicate 3 pointed by i with 9

'''

# Removes duplicates
def removeDuplicates(arr):
  j = 0
  for i in range(0, len(arr)-1): 
    if arr[i] != arr[i+1]: 
        arr[j] = arr[i] 
        j += 1
    print(arr)
  print('total number of duplicates are', j)
  print(arr[:len(arr)-j+1])

# If we can count the total number of duplicates, we can subtract that from the array
def removeDuplicates1(nums):
  i = 0
  # count = 0
  for j in range(1, len(nums)):
    if nums[i] != nums[j]:
      i = i + 1
      nums[i] = nums[j]
    '''
    else:
      count = count + 1 # instead of counting the count, [0, i+1] would hold non duplicated array
    '''
  print(nums[: i+1])
  return i + 1

removeDuplicates1([1, 1, 3, 3, 3, 3, 5, 7, 8, 9])
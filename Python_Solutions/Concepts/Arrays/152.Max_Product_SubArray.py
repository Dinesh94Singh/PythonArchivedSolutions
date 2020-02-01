'''
152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

int temp = max;
            max = Math.max(Math.max(max * A[i], min * A[i]), A[i]);
            min = Math.min(Math.min(temp * A[i], min * A[i]), A[i]);
            if (max > result) {
                result = max;
            }

'''

# def maxProduct(self, nums: List[int]) -> int:

# The below apporach does not solve the use case where there might be two negative numbers - [-2, 3, -4] will result the output as 3 even though -2 * -4 will result in a positive number 8
# curr_product = nums[0]
#           max_product = nums[0]
#           for i in range(1, len(nums)):
#               curr_product = max(nums[i], curr_product*nums[i])
#               max_product = max(max_product, curr_product)
#           return max_product

def maxProduct(nums):
  if not nums:
        return 
  locMin = locMax = gloMax = nums[0]
  # print('local max is ', locMax, ' local min is ', locMin, ' gloMax is ', gloMax)
  for i in range(1, len(nums)):
      if nums[i] < 0:
          tmp = locMax
          locMax = max(locMin*nums[i], nums[i]) # multiple locMax with negative will give a much bigger number than multiplying locMin with negative number
          locMin = min(tmp*nums[i], nums[i])
      else:
          locMax = max(locMax*nums[i], nums[i]) # since it is positive, multiply with max to get maximum results
          locMin = min(locMin*nums[i], nums[i])
      gloMax = max(gloMax, locMax)
      # print('local max is ', locMax, ' local min is ', locMin, ' gloMax is ', gloMax)
  return gloMax

print(maxProduct([2, 3, -2, 4]))
print(maxProduct([-2, 0, -1]))
print(maxProduct([-2, 3, -4]))


def maximum_prod_subarray(nums):
    localMax = nums[0]
    localMin = nums[0]

    globalMax = float('-inf')

    for i in range(1, len(nums)):
        if nums[i] < 0: # if the number if -ve
            # if the localMin is already negative, then the product will give +ve, check this positive res is larger than localMax

            t = localMin
            localMax = max(nums[i], localMin * nums[i])
            localMin = min(nums[i], t * nums[i])
        else:
            # update localMax and localMin
            localMax = max(localMax*nums[i], nums[i])
            localMin = min(localMin*nums[i], nums[i])
        
        globalMax = max(globalMax, localMax)

    return globalMax

print('\n\n')

print(maximum_prod_subarray([2, 3, -2, 4]))
print(maximum_prod_subarray([-2, 0, -1]))
print(maximum_prod_subarray([-2, 3, -4]))
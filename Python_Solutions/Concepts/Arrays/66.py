'''

66. Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

'''

def plusOne(digits):
  digits[-1] += 1 # adds one to last digit
  print(digits)
  for i in range(len(digits)-1, 0, -1):
    # since we are adding 1, the max we could get is 10
    if digits[i] != 10:
      break
    digits[i] = 0
    digits[i-1] += 1
  
  # if the first element gets the carry
  if digits[0] == 10:
    digits[0] = 0
    return [1] + digits
  return digits
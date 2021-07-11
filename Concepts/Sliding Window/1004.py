'''
1004. Max Consecutive Ones III

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.


Interpret the problem as -> Find the longest subarray with at most K zeros.

public int longestOnes(int[] nums, int k) {
    int maxLen = 0;
    for (int lo = 0, hi = 0, zeros = 0; hi < nums.length; hi++) {
        zeros += nums[hi] == 0 ? 1 : 0;
        if (zeros > k) {
            zeros -= nums[lo++] == 0 ? 1 : 0; 
        }
        maxLen = hi - lo + 1;
    }
    return maxLen;
}
'''

def longestOnes(nums, k):
    max_length = 0
    window_start = 0
    zeros = 0 
    for window_end in range(len(nums)):
        zeros += 1 if nums[window_end] == 0 else 0 # Add 1 if the current element is 0
        while zeros > k:
            # when zeros count crosses k
            zeros -= 1 if nums[window_start] == 0 else 0 # increment the window till, we only have k zeros in the window
            window_start += 1
        print('max_length from ', window_start , ' till ', window_end)
        max_length = max(window_end - window_start + 1, max_length)
    return max_length

longestOnes([0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1], 1)
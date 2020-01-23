"""
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
"""

# Enter Code Here

"""
Brute Force Solution - Try all pairs in an linear way.

Time Complexity => O(n^3)
"""
def valid_triangle_number_brute_force(arr):
    count = 0
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] > arr[k]:
                    print(arr[i], arr[j], arr[k])
                    count += 1
    return count

print(valid_triangle_number_brute_force([2, 2, 3, 4]))

def valid_triangle_number_binary_search(arr):
    count = 0
    arr.sort()

    def binary_search(lo, hi, total):
        while lo <= hi and hi < len(arr):
            mid = (lo + hi) // 2
            if arr[mid] >= total:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    for i in range(len(arr) - 2):
        k = i + 2 # min of 3 elements
        for j in range(i + 1, len(arr) - 1):
            k = binary_search(k, len(arr) - 1, arr[i] + arr[j])
            count += (k - j - 1)
    return count
        
print(valid_triangle_number_binary_search([2, 2, 3, 4]))

print(valid_triangle_number_binary_search([1, 1, 3, 4]))

print(valid_triangle_number_binary_search([0, 1, 0]))

#     public int triangleNumber(int[] nums) {
#         int count = 0;
#         Arrays.sort(nums);
#         for (int i = 0; i < nums.length - 2; i++) {
#             int k = i + 2;
#             for (int j = i + 1; j < nums.length - 1 && nums[i] != 0; j++) {
#                 while (k < nums.length && nums[i] + nums[j] > nums[k])
#                     k++;
#                 count += k - j - 1;
#             }
#         }
#         return count;
#     }



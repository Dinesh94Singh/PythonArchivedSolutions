"""
349. Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

l1.sort((a, b) => a - b) // assume sorted
    l2.sort((a, b) => a - b) // assume sorted
    const intersections = []
    let l = 0, r = 0;
    while ((l2[l] && l1[r]) !== undefined) {
       const left = l1[r], right = l2[l];
        if (right === left) {
            intersections.push(right)
            while (left === l1[r]) r++;
            while (right === l2[l]) l++;
            continue;
        }
        if (right > left) while (left === l1[r]) r++;
         else while (right === l2[l]) l++;

    }
    return intersections;

"""


def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()

    res = []

    left, right = 0, 0
    while left < len(nums1) and right < len(nums2):
        left_val = nums1[left]
        right_val = nums2[right]

        if right_val == left_val:
            res.append(nums2[right])
            while right < len(nums2) and nums2[right] == right_val:
                right += 1
            while left < len(nums1) and nums1[left] == left_val:
                left += 1
        if right_val > left_val:
            while left < len(nums1) and left_val == nums1[left]:
                left += 1
        else:
            while right < len(nums2) and right_val == nums2[right]:
                right += 1
    return res


intersection([1, 2, 2, 1], [2, 2])

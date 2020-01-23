import random
import heapq

def kth_largest_number_quick_select(nums, k):
    """
    Time complexity : O(n) (Amortized). If you sort our use heap => (O(nlogn)) or (O(nlogk))
    :param nums: List - that needs to be sorted
    :param k: int - Kth largest number
    :return: int - kth largest number
    """
    def quick_select(lo, hi, index):
        if lo == hi:
            return nums[lo]

        pivot_idx = random.randint(lo, hi) # inclusive range
        nums[pivot_idx], nums[lo] = nums[lo], nums[pivot_idx]

        i = lo
        for j in range(lo + 1, hi + 1):
            if nums[j] < nums[lo]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i], nums[lo] = nums[lo], nums[i]

        if i == index:
            return nums[i]
        if i < index:
            return quick_select(i + 1, hi, index) # there are i elements prior to pivot_ele, you need more
        else:
            return quick_select(lo, i - 1, index) # there are i elements prior to pivot_ele, you need less

    return quick_select(0, len(nums) - 1, len(nums) - k)

print(kth_largest_number_quick_select([1, 5, 2, 3, 8, 10, 4, 6, 25], 1))
print(kth_largest_number_quick_select([1, 5, 2, 3, 8, 10, 4, 6, 25], 2))
print(kth_largest_number_quick_select([1, 5, 2, 3, 8, 10, 4, 6, 25], 3))
print(kth_largest_number_quick_select([1, 5, 2, 3, 8, 10, 4, 6, 25], 4))

def kth_largest_number_heap(nums, k):
    min_heap = []
    i = 0
    while i < len(nums):
        if len(min_heap) < k:
            heapq.heappush(min_heap, nums[i])
        else:
            if min_heap[0] < nums[i]:
                heapq.heapreplace(min_heap, nums[i])
        i += 1
    return min_heap[0]

print(kth_largest_number_heap([1, 5, 2, 3, 8, 10, 4, 6, 25], 1))
print(kth_largest_number_heap([1, 5, 2, 3, 8, 10, 4, 6, 25], 2))
print(kth_largest_number_heap([1, 5, 2, 3, 8, 10, 4, 6, 25], 3))
print(kth_largest_number_heap([1, 5, 2, 3, 8, 10, 4, 6, 25], 4))


def kth_largest_number_brute_force(nums, k):
    return sorted(nums)[-k]

print(kth_largest_number_brute_force([1, 5, 2, 3, 8, 10, 4, 6, 25], 1))
print(kth_largest_number_brute_force([1, 5, 2, 3, 8, 10, 4, 6, 25], 2))
print(kth_largest_number_brute_force([1, 5, 2, 3, 8, 10, 4, 6, 25], 3))
print(kth_largest_number_brute_force([1, 5, 2, 3, 8, 10, 4, 6, 25], 4))

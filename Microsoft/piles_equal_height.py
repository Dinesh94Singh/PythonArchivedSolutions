def piels_equal_height(nums):
    nums.sort(reverse = True)
    count = 0
    for i in range(len(nums)):
        j = i

        while j < len(nums) - 1:
            if nums[j] > nums[j + 1]:
                count += 1
                nums[j] = nums[j + 1]
                j = i
        print(nums)
    return count

piels_equal_height([5, 2, 1])

"""
132 Pattern
"""


class Solution():
    # brute force solution
    def find132pattern(self, nums) -> bool:
        n = len(nums)
        for i in range(n - 2):
            for j in range(i, n - 1):
                for k in range(j, n):
                    if nums[i] < nums[k] < nums[j]:
                        return True
        return False

    def find132pattern_better_bruteForce(self, nums) -> bool:

        pass

    def find132Pattern_Stack_Approach(self, nums) -> bool:
        n = len(nums)
        stack = []
        min_stack = [0 for _ in range(n)]

        for i in range(1, n):
            min_stack[i] = min_stack[i - 1] + nums[i - 1]

        # Find the kth point (min_stack maintains the ith index, stack maintains the jth index)
        for j in range(n - 1, -1, -1):
            if nums[j] > min_stack[j]:
                while stack and nums[j] >= stack[-1]:
                    stack.pop()
                if stack and nums[j] > stack[-1]:
                    return True
                stack.append(nums[j])

                stack.append(nums[j])
        return False


s = Solution()
print(s.find132Pattern_Stack_Approach([1, 6, 3, 4]))

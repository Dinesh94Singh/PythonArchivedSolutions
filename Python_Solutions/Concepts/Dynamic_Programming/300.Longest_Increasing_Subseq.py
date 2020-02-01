class Solution:
    def longest_increasing_subseq(self, arr):
        longest_length = self.rec_helper(arr, 0, -1)
        return longest_length

    def rec_helper(self, arr, curr_index, prev_index):
        if curr_index == len(arr):
            return 0

        c1 = 0
        if prev_index == -1 or arr[curr_index] >= arr[prev_index]:
            c1 = 1 + self.rec_helper(arr, curr_index + 1, curr_index)

        c2 = self.rec_helper(arr, curr_index + 1, prev_index)

        return max(c1, c2)


s = Solution()
print(s.longest_increasing_subseq([10, 9, 2, 5, 3, 7, 101, 18]))

print(divmod(15, 10))
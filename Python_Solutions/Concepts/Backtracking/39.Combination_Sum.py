from typing import List


def combinationSum(arr: List[int], target: int) -> List[List[int]]:
    res = []

    def back_tracking_helper(start, sub_arr, remaining):
        if remaining < 0:
            return

        if remaining == 0:
            res.append(sub_arr)

        for idx in range(start, len(arr)):
            back_tracking_helper(idx, sub_arr + [arr[idx]], remaining - arr[idx])

    back_tracking_helper(0, [], target)
    return res


print(combinationSum([2, 3, 6, 7], 7))

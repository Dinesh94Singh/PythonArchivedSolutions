def solution(arr):
    i = 0
    periods = 0
    while i < len(arr) - 2:
        j = i + 1
        while j < len(arr) - 1:
            if arr[j + 1] - arr[j] == arr[i + 1] - arr[i]:
                periods += 1
                j += 1
            else:
                # i = j this should not be done because, it will skip (6, 8) and (7, 9) paths - refer ipad
                break
        i += 1
    return periods


print(solution([-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]))

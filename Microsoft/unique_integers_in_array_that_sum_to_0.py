def unique_integers_in_array_that_sum_to_0(N):
    if N % 2 == 0:
        # [-2, -1, 1, 2] (for n = 2)
        res = []
    else:
        res = [0]
        N = N - 1 # this would make it even

    for i in range(1, (N // 2) + 1):
        res.append(i)
        res.append(i * -1)
    return res

print(unique_integers_in_array_that_sum_to_0(4))
print(unique_integers_in_array_that_sum_to_0(3))
print(unique_integers_in_array_that_sum_to_0(2))
print(unique_integers_in_array_that_sum_to_0(1))
print(unique_integers_in_array_that_sum_to_0(0))

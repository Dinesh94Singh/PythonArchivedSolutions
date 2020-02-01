def fair_indexes(a, b):
    if len(a) != len(b):
        return 0

    total_a = sum(a)
    total_b = sum(b)

    cumm_a = 0
    cumm_b = 0

    res = 0

    for i in range(len(a) - 1):
        cumm_a += a[i]
        cumm_b += b[i]

        if cumm_a == cumm_b and cumm_a * 2 == total_a and cumm_b * 2 == total_b:
            res += 1

    return res


'''
        int[] A1 = {4,-1,0,3}, B1 = {-2, 5, 0 ,3};
        int[] A2 = {2,-2,-3,3}, B2 = {0,0,4,-4}
        int[] A3 = {4,-1,0,3}, B3 = {-2,6,0,4};
        int[] A4 = {3,2,6}, B4 = {4,1,6};
        int[] A5 = {1,4,2,-2,5}, B5 = {7,-2,-2,2,5};
        int[] A6 = {0, 0, 0}, B6 = {0, 0, 0};
'''

print(fair_indexes([4, -1, 0, 3], [-2, 5, 0, 3]))  # 2
print(fair_indexes([2, -2, -3, 3], [0, 0, 4, -4]))  # 1
print(fair_indexes([4, -1, 0, 3], [-2, 6, 0, 4]))  # 0
print(fair_indexes([3, 2, 6], [4, 1, 6]))  # 0
print(fair_indexes([1, 4, 2, -2, 5], [7, -2, -2, 2, 5]))  # 2
print(fair_indexes([0, 0, 0], [0, 0, 0]))  # 1


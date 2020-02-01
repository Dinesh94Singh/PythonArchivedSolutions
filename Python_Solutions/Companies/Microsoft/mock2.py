def total_number_of_ways_to_climb_stairs(n):
    count = 0

    if n == 0:
        return 0

    def rec_helper(n):
        nonlocal count
        if n == 0:
            count += 1
            return
        if n < 0:
            return

        rec_helper(n - 1)  # make 1 step
        rec_helper(n - 2)  # make 2 step
        rec_helper(n - 3)  # make 3 step

    rec_helper(n)
    return count

# further optimization => Memoization => Tabulation and DP


print(total_number_of_ways_to_climb_stairs(0))
print(total_number_of_ways_to_climb_stairs(1))
print(total_number_of_ways_to_climb_stairs(2))
print(total_number_of_ways_to_climb_stairs(4))
print(total_number_of_ways_to_climb_stairs(3))


def get_matching_paren(s, index):
    if len(s) % 2 != 0:
        return -1  # not a valid string

    if not s or s == '':
        return -1

    stack = []  # stores indexes

    forward_hm = {}
    backward_hm = {}

    for i, each in enumerate(s):
        if each == '(':
            stack.append(i)
        else:
            open_idx = stack.pop()
            forward_hm[open_idx] = i
            backward_hm[i] = open_idx

    if index in forward_hm:
        return forward_hm[index]
    elif index in backward_hm:
        return backward_hm[index]
    else:
        return -1

print(get_matching_paren("((())())", 1))
print(get_matching_paren("((())())", 0))
print(get_matching_paren("((())())", 100))
print(get_matching_paren("((())())", 3))

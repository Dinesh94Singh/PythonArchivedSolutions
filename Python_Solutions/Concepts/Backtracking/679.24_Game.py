def rec_helper(arr):
    if not arr:
        return False
    if len(arr) == 1:
        if abs(arr[0] - 24) < 1e-6:
            print(arr[0])
        return abs(arr[0] - 24) < 1e-6

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                new_arr = [arr[k] for k in range(len(arr)) if i != k != j]

                for each_op in ["/", "-", "+", "*"]:
                    if each_op == '+':
                        new_arr.append(arr[i] + arr[j])
                    if each_op == '-':
                        new_arr.append(arr[i] - arr[j])
                    if each_op == '*':
                        new_arr.append(arr[i] * arr[j])
                    if each_op == '/':
                        if arr[j] != 0:
                            new_arr.append(arr[i] / arr[j])
                        else:
                            continue
                    if rec_helper(new_arr):
                        return True
                    new_arr.pop()
    return False


rec_helper([3, 3, 8, 8])

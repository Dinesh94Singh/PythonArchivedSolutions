from collections import Counter


def check_perm_palindrome(s):
    if s is None:
        return False
    if s == '':
        return True  # considering empty string as an palindrome

    c = Counter(s)
    odd_found = False
    for each in c:
        if c[each] % 2 == 0:
            continue
        elif not odd_found:
            odd_found = True
        else:
            return False
    return True


print(check_perm_palindrome('carrace'))
print(check_perm_palindrome('dinesh'))
print(check_perm_palindrome(''))
print(check_perm_palindrome(None))


def add_angles(s):
    """

    :param s: input string
    :return: string with added angle brackets
    """

    if not s:
        return ''

    stack = []
    start = []

    res = []
    for each in s:
        if each == '>':
            if stack and stack[-1] == '<':
                stack.pop()
            else:
                start.append('<')
        else:
            stack.append(each)

        res += each

    end = ['>' for i in range(len(stack))]
    res += end

    res = start + res

    return ''.join(res) if res != [] else s


print(add_angles("><<><"))
print(add_angles("<><>"))
print(add_angles("<<<<"))
print(add_angles(">>>><<<<"))
print(add_angles("><"))
print(add_angles(""))
print(add_angles(None))
print(add_angles(">>>>>><"))
print(add_angles("<>><><<>"))

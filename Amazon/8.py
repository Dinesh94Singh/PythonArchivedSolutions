def myAtoi(s: str) -> int:
    s = s.strip()

    if s[0] == '-':
        n = s[1:]
    else:
        n = s

    num = 0
    for i in range(len(n)):
        num = num * 10 + ord(n[i]) - ord('0')

    if s[0] == '-':
        return -num
    else:
        return num

print(myAtoi("     -42     "))
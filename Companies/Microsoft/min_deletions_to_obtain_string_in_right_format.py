# def calculate(self, str):
#     right = len(str) - 1
#     left = 0
#     countDict = collections.Counter(str)
#     countA = countDict['A']
#     countB = countDict['B']
#     noOfDel = 0
#     while left < right:
#         if str[left] == 'A':
#             countA = countA - 1
#             left = left + 1
#             continue
#         if str[right] == 'B':
#             countB = countB - 1
#             right = right - 1
#             continue
#
#         if countA != 0 and countB != 0 and countA == countB:
#             noOfDel = noOfDel + 1
#             left = left + 1
#             countB = countB - 1
#             continue
#         if countA > countB:
#             noOfDel = noOfDel + 1
#             left = left + 1
#             countB = countB - 1
#             continue
#
#         if countB > countA:
#             noOfDel = noOfDel + 1
#             right = right - 1
#             countA = countA - 1
#
#     return noOfDel


def calculate(s):
    total_bs = 0
    total_as = 0

    for each in s:
        if each == 'A':
            total_as += 1

    ans = total_as

    for _, each in enumerate(s):
        if each == 'A':
            total_as -= 1
        else:
            total_bs += 1

        ans = min(ans, total_as + total_bs)

    return ans


print(calculate("BAAABAB"))
print(calculate("BBABAA"))

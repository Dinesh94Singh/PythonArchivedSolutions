"""
https://leetcode.com/discuss/interview-question/398026/
"""

def min_moves(st):
    i, j, count = 0, len(st)-1, 0
    while i+2 < j:
        view = st[i:i+3]
        if view == 'aaa':
            count += 1
            i += 2
        elif view == 'bbb':
            count +=1
            i += 2
        i+=1
    return count

print(min_moves("baaaaa"))
print(min_moves("baaabbaabbba"))
print(min_moves("baabab"))

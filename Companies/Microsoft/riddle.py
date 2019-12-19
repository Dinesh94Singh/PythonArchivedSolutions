import string
import random
import re

"""
    - Prefer this
    T(C) => O(N + C) where C is the time taken for the random generator 
    N is the total length of the String
"""
def replaceQuestionMark_random_approach(s):
    def replace(s, i):
        rand = 0
        c = ''

        while True:
            rand = random.randint(0, 25)
            c = chr(97 + rand)

            if not (i > 0 and s[i - 1] == c) or (i < len(s) - 1 or s[i + 1] == c):
                break
        s[i] = c
        return s

    if len(s) == 0:
        return

    s = list(s)

    for i in range(len(s)):
        if s[i] == "?":
            s = replace(s, i)

    return ''.join(s)


def replaceQuestionMark(puzzle):
    # find question marks and iterate through all of them
    for data in re.finditer(r'\?',puzzle):
        # if the question mark is at the start of the string puzzle exclude only the character following it
        if data.span()[0] == 0:
            excludeChar = puzzle[(data.span()[0]+1):(data.span()[1]+1)]
        # if the question mark is at the end of the string puzzle exclude only the character preceding it
        elif data.span()[1] == len(puzzle):
            excludeChar = puzzle[(data.span()[0]-1):(data.span()[1]-1)]
        # else exclude characters on both the sides of question mark
        else:
            excludeChar = puzzle[(data.span()[0]-1):(data.span()[1]-1)] + puzzle[(data.span()[0]+1):(data.span()[1]+1)]
        # substitute each question mark one by one with random choice of lowercase characters excluding the exclude character
        puzzle= re.sub(r'\?',random.choice([i for i in string.ascii_lowercase if i not in excludeChar]),puzzle,count=1)
    return puzzle

# this is the driving code to test the three examples here
# print(replaceQuestionMark('xy?xz?'))
# print(replaceQuestionMark('ab?e?mr??'))
# print(replaceQuestionMark('??????'))
"""
Sample Output:
xyjxzm
abzeqmrdn
utbmda
"""

print(replaceQuestionMark_random_approach('xy?xz?'))
print(replaceQuestionMark_random_approach('ab?e?mr??'))
print(replaceQuestionMark_random_approach('??????'))
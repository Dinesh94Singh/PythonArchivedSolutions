"""
Comparing Strings containing Backspaces (medium)
Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

Example 1:

Input: str1="xy#z", str2="xzz#"
Output: true
Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
Example 2:

Input: str1="xy#z", str2="xyz#"
Output: false
Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
Example 3:

Input: str1="xp#", str2="xyz##"
Output: true
Explanation: After applying backspaces the strings become "x" and "x" respectively.
In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
Example 4:

Input: str1="xywrrmp", str2="xywrrmu#p"
Output: true
Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.
"""


def backspace_compare(str1, str2):
    def format_str(s):
        a = list(s)
        prev = -1
        i = 0
        count = 0
        while i < len(a):
            print(a[i])
            if a[i] == '#':
                count += 1
            else:
                for back_pos in range(count):
                    if prev == 0:
                        continue
                    prev -= 1
                count = 0
                prev += 1
                a[prev] = a[i]
            i = i + 1
        if count > 0:
            for back_pos in range(count):
                if prev == 0:
                    continue
                prev -= 1
        return ''.join(a[:prev+1])
    s1 = format_str(str1)
    s2 = format_str(str2)
    print(s1, s2)
    return s1 == s2


backspace_compare("xywrrmu#p", "xvwrrmp")
backspace_compare("xywrr##mu#p", "xvwmp")
backspace_compare("xy#z", "xyz#")
backspace_compare("xy#z", "xzz#")
backspace_compare("xp#", "xyz##")

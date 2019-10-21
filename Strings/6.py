"""

6. Zigzag conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

"""


def convert(s, num_rows):
    n = len(s)
    matrix = [[] for x in range(num_rows)]
    i = 0
    while i < n:
        for j in range(num_rows):
            if i >= n:
                break
            matrix[j].append(s[i])
            i += 1
        for j in range(num_rows - 2, 0, -1):
            if i >= n:
                break
            matrix[j].append(s[i])
            i += 1
    # Flatten the matrix
    return ''.join([''.join(row) for row in matrix])


convert("PAYPALISHIRING", 4)

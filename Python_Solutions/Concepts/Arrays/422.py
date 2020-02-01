"""
Given a sequence of words, check whether it forms a valid word square.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

Note:
The number of words given is at least 1 and does not exceed 500.
Word length will be at least 1 and does not exceed 500.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
[
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]

Output:
true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crmy".
The fourth row and fourth column both read "dtye".

Therefore, it is a valid word square.
Example 2:

Input:
[
  "abcd",
  "bnrt",
  "crm",
  "dt"
]

Output:
true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crm".
The fourth row and fourth column both read "dt".

Therefore, it is a valid word square.
Example 3:

Input:
[
  "ball",
  "area",
  "read",
  "lady"
]

Output:
false

Explanation:
The third row reads "read" while the third column reads "lead".

Therefore, it is NOT a valid word square.
"""

def validWordSquare(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if len(a[i]) <= j or j >= len(a) or len(a[j]) <= i:
                return False
            if a[i][j] != a[j][i]:
                return False
    return True
word_list_1 = [
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]
word_list_2 = [
  "ball",
  "area",
  "read",
  "lady"
]
word_list_3 = [
  "abcd",
  "bnrt",
  "crm",
  "dt"
]
word_list_4 = [
"ball",
"asee",
"let",
"lep"
]

word_list_5 = [
"abc",
"b"
]
word_list_6 = [
"abc",
"a"
]
validWordSquare(word_list_6)

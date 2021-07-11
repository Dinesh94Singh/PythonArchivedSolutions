"""

79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

"""


# def exist(self, board: List[List[str]], word: str) -> bool:

def exist(board, word):
    if not board:
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, i, j, word):
                return True


def dfs(board, i, j, word):
    if len(word) == 0:
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return False
    temp = board[i][j]
    # instead of creating a new 2D array each time, modify inplace.
    # also helps in not visiting the same node again by forming a cycle
    board[i][j] = '#'
    res = dfs(board, i + 1, j, word[1:]) or dfs(board, i - 1, j, word[1:]) or dfs(board, i, j + 1, word[1:]) or dfs(
        board, i, j - 1, word[1:])
    board[i][j] = temp
    return res


def retry(board, word):
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0

    ans = False

    def dfs(r, c, word):
        nonlocal ans
        print(word)
        if word == '':
            ans = True

        temp = board[r][c]
        board[r][c] = '#'

        res = False
        for row, col in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:

            if 0 <= row < rows and 0 <= col < cols:
                if board[row][col] == word[0]:
                    res = res or dfs(row, col, word[1:])

        board[r][c] = temp
        return res

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0]:
                dfs(i, j, word[1:])

    return ans

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = 'ABCCED'
retry(board, word)
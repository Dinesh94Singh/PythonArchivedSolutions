"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]


Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""


class My_Solution:
    def findWords(self, board, words):

        def check_cond(row, col):
            if 0 <= row < len(board) and 0 <= col < len(board):
                return True
            return False

        def back_track(row, col, word, visited, path):
            nonlocal res
            if word == '':
                res.append(path)
            dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for each_dir in dir:
                if check_cond(row + each_dir[0], col + each_dir[1]) and board[row + each_dir[0]][
                    col + each_dir[1]] == word[: 1]:
                    # mark this visited and do a back_track call
                    board[i][j] = 'X'
                    back_track(row + each_dir[0], col + each_dir[1], word[1:], None, path + word[: 1])

        res = []
        temp = board
        for word in words:
            board = temp
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[: 1]:
                        board[i][j] = 'X'
                        back_track(i, j, word[1:], None, word[: 1])
        return res


s = Solution()

board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]
words = ["oath", "pea", "eat", "rain", "at"]

print(s.findWords(board, words))

##########################################################

import collections


class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
        self.data = None


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
        node.data = word

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
            if not node:
                return False
        return node.isWord


class LeetCodeSolution(object):
    def find_words(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#" # Mark Visisted in this path :P
        self.dfs(board, node, i + 1, j, path + tmp, res) # instead of path, use node.data
        self.dfs(board, node, i - 1, j, path + tmp, res)
        self.dfs(board, node, i, j - 1, path + tmp, res)
        self.dfs(board, node, i, j + 1, path + tmp, res)
        board[i][j] = tmp

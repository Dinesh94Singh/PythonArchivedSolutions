"""
36. Validate Sudoku
"""


class Solution:
    def is_valid_sudoku(self, board):
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele != '.':
                    box_idx = (i // 3) * 3 + (j // 3)

                    if ele in row[i] or ele in col[j] or ele in boxes[box_idx]:
                        return False
                    row[i].add(ele)
                    col[j].add(ele)
                    boxes[box_idx].add(ele)

        return True


s = Solution()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
s.is_valid_sudoku(board)

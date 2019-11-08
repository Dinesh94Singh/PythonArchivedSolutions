"""
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:

Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?

"""


class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.size = n
        self.grid = [[0 for _ in range(n)] for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            Exception('Not a valid row and col index')

        # when player 1 makes a move - +1, when player 2 makes a move -1
        move = 1 if player == 1 else -1
        self.grid[row][col] = move # update the grid with the move.

        # check if player has won the game

        # check same column =>
        col_check = False
        total = 0
        for j in range(self.size):
            total += self.grid[row][j] # row constant
        if abs(total) == self.size:
            col_check = True

        # check same row
        row_check = False
        total = 0
        for j in range(self.size):
            total += self.grid[j][col] # col constant
        if abs(total) == self.size:
            row_check = True

        # check diagonals
        diag_check, rev_diag_check = False, False
        total = 0
        for i in range(self.size):
            total += self.grid[i][i]
        if abs(total) == self.size:
            diag_check = True

        total = 0
        for i in range(self.size):
            print('rev diag => [', i, ', ', self.size -i - 1, ']')
            total += self.grid[self.size - i - 1][i]
        print(total, 'iss the total')
        if abs(total) == self.size:
            rev_diag_check = True

        print(self.grid)
        if col_check or row_check or diag_check or rev_diag_check:
            # print(player, 'has won')
            return player # player has won
        return 0




# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

# obj = TicTacToe(3)
# print(obj.move(0, 0, 1))
# print(obj.move(0, 2, 2))
# print(obj.move(1, 0, 1))
# print(obj.move(1, 2, 2))
# print(obj.move(2, 0, 1))
# print(obj.move(2, 2, 2))

"""
["TicTacToe","move","move","move"]
[[2],[0,1,1],[1,1,2],[1,0,1]]
"""

obj = TicTacToe(2)
obj.move(0, 1, 1)
print('\n\n')
obj.move(1, 1, 2)
print('\n\n')
obj.move(1, 0, 1)
print('\n\n')
# print(obj.move(0, 1, 1))
# print(obj.move(1, 1, 2))
# print(obj.move(1, 0, 1))
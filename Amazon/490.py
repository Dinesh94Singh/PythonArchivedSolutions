"""
The Maze

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down,
left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the
borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.
"""
from collections import deque


class Solution:
    def has_path(self, maze, start, destination):
        q = deque([start])
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            node = q.popleft()
            maze[node[0]][node[1]] = 'X'  # mark visited.
            if node[0] == destination[0] and node[1] == destination[1]:
                return True
            for each_dir in dir:
                row = node[0] + each_dir[0]
                col = node[1] + each_dir[1]
                while 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == 0:
                    # keep rolling till you hit the end
                    row += each_dir[0]
                    col += each_dir[1]
                # it failed because of adding row and col, so subtract the last one
                row -= each_dir[0]  # from the place you hit a boundary - find a way to reach the destination
                col -= each_dir[1]

                if maze[row][col] == 0:
                    q.append([row, col])
        return False


grid = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]

s = Solution()
print(s.has_path(grid, [0, 4], [4, 4]))

grid2 = [[0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0],
         [1, 1, 0, 1, 1],
         [0, 0, 0, 0, 0]]

print(s.has_path(grid, [0, 4], [3, 2]))
print(s.has_path(grid, [0, 4], [1, 2]))

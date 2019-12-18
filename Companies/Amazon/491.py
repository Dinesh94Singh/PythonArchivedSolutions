"""There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down,
left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the
destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (
excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the
borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.


Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.



Note:

There is only one ball and one destination in the maze. Both the ball and the destination exist on an empty space,
and they will not be at the same position initially. The given maze does not contain border (like the red rectangle
in the example pictures), but you could assume the border of the maze are all walls. The maze contains at least 2
empty spaces, and both the width and height of the maze won't exceed 100. """

from collections import deque


class Solution:
    def shortestDistance(self, maze, start, destination) -> int:
        q = deque([(start, 0)])
        visited = set()
        visited.add((start[0], start[1]))
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        min_dist = float('inf')
        while q:
            n = len(q)
            print(q)
            print(visited)
            for _ in range(n):
                node, d = q.popleft()
                if node[0] == destination[0] and node[1] == destination[1]:
                    print(min_dist, 'so far', distance, 'is the new distance')
                    if min_dist > distance:
                        min_dist = distance
                # print('Level is', distance + 1)
                for each_dir in directions:
                    r = each_dir[0] + node[0]
                    c = each_dir[1] + node[1]
                    distance = d + 1

                    # print('r and c are', r, c)

                    while 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == 0:
                        # print(r, c)
                        r += each_dir[0]
                        c += each_dir[1]
                        distance += 1

                    r -= each_dir[0]
                    c -= each_dir[1]
                    distance -= 1

                    if (r, c) not in visited:
                        q.append(([r, c], distance))
                        visited.add((r, c))
            print('\n')

        return min_dist if min_dist != float('inf') else -1


grid = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]

grid2 = [[0, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 1],
         [0, 0, 0, 0, 1, 0, 0]]

s = Solution()
# print(s.shortestDistance(grid, [0, 4], [4, 4]))
print(s.shortestDistance(grid2, [0, 0], [8, 6]))

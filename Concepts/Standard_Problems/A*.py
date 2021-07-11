"""

A* Algorithm - Best Algorithm to find the shortest path from start till goal

Dijkstra's is an variant of A* algorithm, where Heuristic value for each node is 0


So when to use DFS over A*, when to use Dijkstra over A* to find the shortest paths ?
We can summarise this as below-

1) One source and One Destination-
→ Use A* Search Algorithm (For Unweighted as well as Weighted Graphs)

2) One Source, All Destination –
→ Use BFS (For Unweighted Graphs)
→ Use Dijkstra (For Weighted Graphs without negative weights)
→ Use Bellman Ford (For Weighted Graphs with negative weights)

3) Between every pair of nodes-
→ Floyd-Warshall
→ Johnson’s Algorithm

LeetCode Problems:
=================
    - https://leetcode.com/problems/sliding-puzzle/solution/

Sources:
=======
    - https://www.youtube.com/watch?v=vP5TkF0xJgI
"""

import itertools
import heapq


class Solution(object):
    def slidingPuzzle(self, board):
        rows, cols = len(board), len(board[0])
        start = tuple(itertools.chain(*board))
        target = [i for i in range(1, rows * cols)] + [0]

        # map for rows, col => 1d arrayed value
        expected = {(cols * r + c + 1) % (rows * cols): (r, c)
                    for r in range(rows) for c in range(cols)}

        target_wrong = tuple([i for i in range(1, rows * cols - 2)] + [rows * cols - 1, rows * cols - 2, 0])
        pq = [(0, 0, start, start.index(0))]
        cost = {start: 0}

        expected = {(cols * r + c + 1) % (rows * cols): (r, c)
                    for r in range(rows) for c in range(cols)}

        print(expected, 'is expected')
        print(target_wrong, 'is target_wrong')

        """
            -> A heuristic function could be as simple as euclidean distance
        """

        def heuristic(state):
            ans = 0
            for r in range(rows):
                for c in range(cols):
                    val = state[cols * r + c]
                    if val == 0:
                        continue
                    er, ec = expected[val]
                    ans += abs(r - er) + abs(c - ec)
            return ans

        while pq:
            # f = estimated distance (priority)
            # g = actual distance travelled (depth)
            f, g, board, zero = heapq.heappop(pq)
            if board == target:
                return g
            if board == target_wrong:
                # if you end up here, you will never be able to solve
                return -1
            if f > cost[board]:
                continue

            for delta in (-1, 1, -cols, cols):
                nei = zero + delta
                if abs(zero // cols - nei // cols) + abs(zero % cols - nei % cols) != 1:
                    continue
                if 0 <= nei < rows * cols:
                    new_board = list(board)
                    new_board[zero], new_board[nei] = new_board[nei], new_board[zero]
                    new_state = tuple(new_board)
                    # f(n) = g(n) + h(n) => where g(n) => g + 1
                    n_cost = g + 1 + heuristic(new_state)
                    if n_cost < cost.get(new_state, float('inf')):
                        cost[new_state] = n_cost
                        heapq.heappush(pq, (n_cost, g + 1, new_state, nei))

        return -1


s = Solution()
board = [[1, 2, 3], [4, 0, 5]]
s.slidingPuzzle(board)

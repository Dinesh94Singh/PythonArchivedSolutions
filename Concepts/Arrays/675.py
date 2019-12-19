"""You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map,
in this map:

0 represents the obstacle can't be reached. 1 represents the ground can be walked through. The place with number
bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.


You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with
lowest height first. And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the
trees. If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:

Input:
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6


Example 2:

Input:
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1


Example 3:

Input:
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.

"""

import heapq


def cut_off_tree(forest):
    m, n = len(forest), len(forest[0])
    heap = [(forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j] > 1]
    heapq.heapify(heap)

    def get_distance(x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            return 0
        queue, dist, visited = [(x1, y1)], 0, {(x1, y1)}
        while queue:
            new_queue = []
            dist += 1
            for r, c in queue: # instead of n and for _ in range(n) -> pop, we can do this.
                for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dir[0], c + dir[1]
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and forest[nr][nc] != 0:
                        visited.add((nr, nc))
                        if nr == x2 and nc == y2:
                            return dist
                        new_queue.append((nr, nc))
            queue = new_queue
        return -1

    res = 0
    x, y = 0, 0
    while heap:
        _, nx, ny = heapq.heappop(heap)  # get the minimum
        dist = get_distance(x, y, nx, ny)
        if dist == -1:
            return -1
        res += dist
        x, y = nx, ny

    return res


forest = [[2, 3, 4],
          [0, 0, 5],
          [8, 7, 6]]
cut_off_tree(forest)

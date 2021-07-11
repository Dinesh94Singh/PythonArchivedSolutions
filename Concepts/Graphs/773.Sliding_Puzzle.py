from typing import List
import itertools
import collections


def slidingPuzzle(board: List[List[int]]) -> int:
    initial_state = tuple(itertools.chain(*board))
    rows, cols = len(board), len(board[0])

    final_state = tuple([i for i in range(1, rows * cols)] + [0])

    initial_cost = 0

    dq = collections.deque([(initial_cost, initial_state.index(0), initial_state)])
    seen = {initial_state}

    while dq:
        cost, zero_idx, curr_state = dq.popleft()

        if curr_state == final_state:
            return cost

        for each_dir in (1, -1, cols, -cols):
            nei = zero_idx + each_dir

            if not (0 <= nei < rows * cols):
                continue

            new_state = list(curr_state)
            new_state[zero_idx], new_state[nei] = new_state[nei], new_state[zero_idx]

            new_state = tuple(new_state)

            if new_state in seen:
                continue

            seen.add(new_state)
            dq.append((cost + 1, nei, new_state))

    return -1


board = [[1, 2, 3], [4, 0, 5]]
print(slidingPuzzle(board))

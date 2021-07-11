from collections import deque

def how_many_flips(source, target):
    q = deque([(source, 0)])
    visited = set()
    while q:
        n = len(q)
        for _ in range(n):
            intermediate_word, level = q.popleft()
            if intermediate_word == target:
                return level
            visited.add(intermediate_word)
            for idx in range(len(intermediate_word)):
                ch = intermediate_word[idx]
                flipped_ch = '1' if ch == '0' else '0'
                new_word = intermediate_word[:idx] + flipped_ch + intermediate_word[idx + 1:]
                if new_word not in visited:
                    q.append((new_word, level + 1))

    return -1 # target word not found

print(how_many_flips('00000', '01011'))
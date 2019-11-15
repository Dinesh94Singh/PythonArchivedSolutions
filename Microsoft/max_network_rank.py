def dfs(visited, map, j):
    if j in visited or j not in map:
        return 0
    visited.add(j)
    nodes = map[j]
    l = len(nodes)
    for each in nodes:
        if each not in visited:
            l += dfs(visited, map, each)
    return l


def countEdges(A, B, N):
    if A is None or B is None or len(A) == 0 or len(B) == 0 or len(A) != len(B):
        return 0
    map = {}
    for i in range(len(A)):
        if A[i] not in map:
            map[A[i]] = []
        if B[i] not in map:
            map[B[i]] = []
        map[A[i]].append(B[i])
        map[B[i]].append(A[i])

    visited = set()
    result = 0

    for j in range(1, N + 1):
        if j not in visited:
            edges = dfs(visited, map, j)
            result = max(result, edges)
    return result // 2
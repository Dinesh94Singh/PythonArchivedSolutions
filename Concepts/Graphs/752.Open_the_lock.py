import collections


class Solution(object):
    def openLock(self, deadends, target):
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    # in python % is modulos, in java and other lang's % is remainder.
                    # for other languages => (x + d + 10) % 10
                    y = (x + d + 10) % 10
                    yield node[:i] + str(y) + node[i + 1:]

        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            if node in dead:
                continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth + 1))
        return -1


s = Solution()
deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
s.openLock(deadends, target)

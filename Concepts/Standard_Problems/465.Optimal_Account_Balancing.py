import collections


class Solution:
    def optimal_account_balancing(self, transactions):
        graph = collections.defaultdict(int)

        for each in transactions:
            graph[each[0]] += each[2]
            graph[each[1]] -= each[2]

        balance = []

        for each in graph.values():
            if each != 0:
                balance.append(each)

        return self._traverse(0, balance)

    def _traverse(self, idx, balance):
        if idx == len(balance):
            return 0

        curr = balance[idx]
        if curr == 0:
            return self._traverse(idx + 1, balance)

        minimum = float('inf')
        for i in range(idx + 1, len(balance)):
            nxt = balance[i]

            if curr * nxt < 0:
                balance[i] = curr + nxt
                minimum = min(minimum, 1 + self._traverse(idx + 1, balance))
                balance[i] = nxt

                if curr + nxt == 0:
                    break
        return minimum


s = Solution()
print(s.optimal_account_balancing([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]))

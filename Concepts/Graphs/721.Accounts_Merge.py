from typing import List
import collections

class UnionFind:
    def __init__(self):
        self.parent = [i for i in range(10000)]

    def union(self, c1, c2):
        r1, r2 = self.find(c1), self.find(c2)
        if r1 != r2:
            self.parent[r2] = self.parent[r1]

    def find(self, c1):
        if self.parent[c1] != c1:
            self.parent[c1] = self.find(self.parent[c1])
        return self.parent[c1]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = UnionFind()

        email_to_name = {}
        email_to_id = {}
        id = 0

        for each_acc in accounts:
            name = each_acc[0]
            for email in each_acc[1:]:
                email_to_name[email] = name
                if email not in email_to_id:
                    email_to_id[email] = id
                    id += 1
                dsu.union(email_to_id[each_acc[1]], email_to_id[email])

        ans = collections.defaultdict(list)
        for each_mail in email_to_id:
            ans[dsu.find(email_to_id[each_mail])].append(each_mail)  # find will get the parent_id -> email

        res = [[email_to_name[ans[each_id][0]]] + sorted(ans[each_id]) for each_id in ans]
        return res



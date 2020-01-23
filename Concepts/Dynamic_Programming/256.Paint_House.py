from typing import List

class Solution_BruteForce:
    def minCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        min_cost = float('inf')
        
        def rec_helper(house_idx, prev_color, total):
            nonlocal N, min_cost
            if house_idx == N:
                min_cost = min(min_cost, total)
                return
            
            for i in range(3):
                if i != prev_color:
                    rec_helper(house_idx + 1, i, total + costs[house_idx][i])
            
            return
        
        rec_helper(0, -1, 0)
        return min_cost

s = Solution_BruteForce()
print(s.minCost([[17,2,17],[16,16,5],[14,3,19]]))


class Solution_Memoization:
    def minCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        min_cost = float('inf')
        
        cache = [[-1 for _ in range(4)] for _ in range(N)]
        
        def rec_helper(house_idx, prev_color, cache):
            nonlocal N, min_cost
            if house_idx == N:
                return 0
            
            if cache[house_idx][prev_color] != -1:
                return cache[house_idx][prev_color]
       
            min_val = float('inf')
            for i in range(3):
                if i != prev_color:
                    min_val = min(min_val, costs[house_idx][i] + rec_helper(house_idx + 1, i, cache))
            
            cache[house_idx][prev_color] = min_val
            return cache[house_idx][prev_color]
        
        return min([rec_helper(0, i, cache) for i in range(3)])

s = Solution_Memoization()
print(s.minCost([[17,2,17],[16,16,5],[14,3,19]]))
print(s.minCost([[8, 8, 8]]))
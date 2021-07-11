from typing import List

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        N = len(costs)
        K = len(costs[0]) if N > 0 else 0
        
        if N == 0 and K == 0:
            return 0
        
        cache = [[-1 for _ in range(K)] for _ in range(N)]
        def rec_helper(house_idx, color_idx, cache):
            if house_idx == N:
                return 0
            
            if cache[house_idx][color_idx] != -1:
                return cache[house_idx][color_idx]
            
            min_val = float('inf')
            for i in range(K):
                if i != color_idx:
                    min_val = min(min_val, costs[house_idx][i] + rec_helper(house_idx + 1, i, cache))
                    
            cache[house_idx][color_idx] = min_val
            return cache[house_idx][color_idx]
        
        return min([rec_helper(0, i, cache) for i in range(K)])

s = Solution()
print(s.minCostII([[8]]))
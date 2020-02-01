from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        
        start = 0
        end = 1
        
        res = []
        
        while i < n and intervals[i][end] < newInterval[start]:
            res.append(intervals[i])
            i += 1

        print('res so far', res)
            
        while i < n and intervals[i][start] <= newInterval[end] and newInterval[start] <= intervals[i][end]:
            newInterval = [min(intervals[i][start], newInterval[start]), max(intervals[i][end], newInterval[end])]
            i += 1
            
        res.append(newInterval)
        
        while i < n:
            res.append(intervals[i])
            i += 1
            
        return res
                
            
s = Solution()
# print(s.insert([[1,3],[6,9]], [2, 5]))
# print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]))
print(s.insert([[1, 5]], [5, 7]))
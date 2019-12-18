'''
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

'''

# def merge(self, intervals: List[List[int]]) -> List[List[int]]:

def merge(intervals):
  if not intervals:
    return []
  '''
    We need to sort because consider the input as [1, 4], [0, 4]
    If we don't sort the output would be [1, 4], since we are only considering if 0 > 4
  '''
  intervals = sorted(intervals, key = lambda x: x[0])
  res = []
  start = intervals[0][0]
  end = intervals[0][1]
  for i in range(1, len(intervals)):
      if intervals[i][0] > end:
          res.append([start,end])
          start = intervals[i][0]
          end = intervals[i][1]
      else:
          end = max(end, intervals[i][1])
  res.append([start, end])
  return res

merge([[1,3],[2,6],[8,10],[15,18]])
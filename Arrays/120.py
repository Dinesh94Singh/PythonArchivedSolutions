'''
120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''

'''
You cannot apply sorting here because, in the question it is given that you can only use adjacent numbers on the row below.


triangle[i][j] can only add up to triangle[i+1][j-1] or triangle[i+1][j+1]
'''

'''
Dynamic Programming

1. Top-bottom approach
2. Bottom-top approach

Top-bottom approach - recursively find minium path sum of each node. Store the min when you reach new row everytime. But to find the min, we need to store the path sum in an array. Like this for each row, we need array making the space complexity O(n^2)


Bottom-Top approach - Since, base nodes are the leaf nodes, use these to find the min. At kth row the ith node would be cal as

minPath[k][i] = min(minPath[k+1][i], minPath[k+1][i+1]) + triangle[k][i]

But minPath is still an 2D array making the space - O(n^2)

So, instead make it a 1D array and cal minPath at each level.

minPath[i] = min(minPath[i], minPath[i+1]) + triangle[k][i]

(or)

Modify the input array itself like Line 37.

Question: y [i][j] and [i+1][j] ??
input =>
[
  [2],
  [3,4], for 4 the adjacent elements are 5 and 7.
  [6,5,7],
  [4,1,8,3]
] 

one of the adjacent element is at the same index but in the next row. i.e why, we have triangle[i+1][js]
'''



''' Bottom-Up solution'''
def minimum_total_modify_input(triangle):
  n = len(triangle)
  for i in range(n-2, -1, -1):
    for j in range(len(triangle[i])):
      triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
  return triangle[0][0]

# if modifying the input is not allowed.

def minimum_total_N_Space(triangle):
  res = triangle[-1]
  for i in range(len(triangle)-2, -1, -1):
    for j in range(len(triangle[i])):
      res[j] = min(res[j], res[j+1]) + triangle[i][j]
  return res[0]


'''Top-Down Solution'''
def minimum_total_modify_input_top_down(triangle):
  for i in range(1, len(triangle)):
    for j in range(len(triangle[i])):
      if j == 0:
        triangle[i][j] += triangle[i-1][j]
      elif j == len(triangle[i]) - 1:
        triangle[i][j] += triangle[i-1][j-1]
      else:
        triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
  return min(triangle[-1])
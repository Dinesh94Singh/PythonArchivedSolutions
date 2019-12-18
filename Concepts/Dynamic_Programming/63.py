
def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """

    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    # If the starting cell has an obstacle, then simply return as there would be
    # no paths to the destination.
    if obstacleGrid[0][0] == 1:
        return 0

    # Number of ways of reaching the starting cell = 1.
    obstacleGrid[0][0] = 1

    # Filling the values for the first column
    for i in range(1,m):
        obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

    # Filling the values for the first row
    for j in range(1, n):
        obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

    print(obstacleGrid)

    # Starting from cell(1,1) fill up the values
    # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
    # i.e. From above and left.
    for i in range(1,m):
        for j in range(1,n):
            if obstacleGrid[i][j] == 0:
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
            else:
                obstacleGrid[i][j] = 0

    # Return value stored in rightmost bottommost cell. That is the destination.
    return obstacleGrid[m-1][n-1]


"""
*****************
((((((((())))))))
!!!!!!!!!!!!!!!!!
Few Other Solutions
!!!!!!!!!!!!!!!!!!
((((((((()))))))))
******************
"""

# O(m*n) space
# def uniquePathsWithObstacles1(self, obstacleGrid):
#     if not obstacleGrid:
#         return
#     r, c = len(obstacleGrid), len(obstacleGrid[0])
#     dp = [[0 for _ in range(c)] for _ in range(r)]
#     dp[0][0] = 1 - obstacleGrid[0][0]
#     for i in range(1, r):
#         dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])
#     for i in range(1, c):
#         dp[0][i] = dp[0][i-1] * (1 - obstacleGrid[0][i])
#     for i in range(1, r):
#         for j in range(1, c):
#             dp[i][j] = (dp[i][j-1] + dp[i-1][j]) * (1 - obstacleGrid[i][j])
#     return dp[-1][-1]
#
# # O(n) space
# def uniquePathsWithObstacles2(self, obstacleGrid):
#     if not obstacleGrid:
#         return
#     r, c = len(obstacleGrid), len(obstacleGrid[0])
#     cur = [0] * c
#     cur[0] = 1 - obstacleGrid[0][0]
#     for i in range(1, c):
#         cur[i] = cur[i-1] * (1 - obstacleGrid[0][i])
#     for i in range(1, r):
#         cur[0] *= (1 - obstacleGrid[i][0])
#         for j in range(1, c):
#             cur[j] = (cur[j-1] + cur[j]) * (1 - obstacleGrid[i][j])
#     return cur[-1]
#
# # in place
# def uniquePathsWithObstacles(obstacleGrid):
#     if not obstacleGrid:
#         return
#     r, c = len(obstacleGrid), len(obstacleGrid[0])
#     obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
#     for i in range(1, r):
#         obstacleGrid[i][0] = obstacleGrid[i-1][0] * (1 - obstacleGrid[i][0])
#     for i in range(1, c):
#         obstacleGrid[0][i] = obstacleGrid[0][i-1] * (1 - obstacleGrid[0][i])
#     for i in range(1, r):
#         for j in range(1, c):
#             obstacleGrid[i][j] = (obstacleGrid[i-1][j] + obstacleGrid[i][j-1]) * (1 - obstacleGrid[i][j])
#     return obstacleGrid[-1][-1]
#


grid = [[0,0,0],
        [0,1,0],
        [0,1,0]]
grid2 = [[1]]
grid3 = [[0, 0]]
grid4 = [[0]]
grid5 = [[0,0,0,0],
         [0,1,0,0],
         [0,0,0,0],
         [0,0,1,0],
         [0,0,0,0]] # output = 7

print(uniquePathsWithObstacles(grid))
# print(uniquePathsWithObstacles(grid2))
# print(uniquePathsWithObstacles(grid3))
# print(uniquePathsWithObstacles(grid4))
# print(uniquePathsWithObstacles(grid5))

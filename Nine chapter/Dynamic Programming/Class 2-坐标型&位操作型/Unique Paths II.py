# Description
# Follow up for "Unique Paths":
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# m and n will be at most 100.
#
# Example
# Example 1:
# Input: [[0]]
# Output: 1
#
# Example 2:
# Input: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
# Output: 2
# Explanation:
# Only 2 different path.


#动态规划，一共有五种情况要考虑，一是如果[i][j]格有障碍，直接赋值0.二是左上角的点赋值1。三/四是第一行、列取值要根据该行、列有没有障碍，而不是直接设定了是1。五是除这些点之外的点，直接正常等于左边加上面。
# 时间复杂度O(n*m)
# 遍历一遍网格，复杂度即网格大小
# 空间复杂度O(n*m)
# 需要开一个数组记录当前路径数量
class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if obstacleGrid is None:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j >0:
                    dp[i][j] += dp[i][j - 1]
        return dp[m-1][n-1]


    #优化思路，跟Class 1种unique paths优化思路一样，可以只用一个一维数组。


    #记忆化搜索，待扩展

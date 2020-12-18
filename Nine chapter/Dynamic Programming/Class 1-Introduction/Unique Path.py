# Description
# A robot is located at the top-left corner of a m x n grid.
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.
#
# How many possible unique paths are there?
#
# m and n will be at most 100.
# The answer is guaranteed to be in the range of 32-bit integers
#
# Have you met this question in a real interview?
# Example
# Example 1:
#
# Input: n = 1, m = 3
# Output: 1
# Explanation: Only one path to target position.
# Example 2:
#
# Input:  n = 3, m = 3
# Output: 6
# Explanation:
# 	D : Down
# 	R : Right
# 	1) DDRR
# 	2) DRDR
# 	3) DRRD
# 	4) RRDD
# 	5) RDRD
# 	6) RDDR

# 求组合数
# 不难发现，机器人从左上角走到右下角，需要向下走m - 1步，向右走n - 1步，那么总步数也是一定的，为m + n - 2步。问题就转化成，从m + n - 2步中选出m - 1步向下，其余步数自然是向右，有多少种组合？
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        if m == 1 or n == 1:
            return 1
        temp1 = 1
        temp2 = 1
        for i in range(1, m):
            temp1 *= i
        for j in range(n, m + n - 1):
            temp2 *= j
        return temp2//temp1

# 动态规划
# 建立二维数组dp，令dp[i][j]表示到达 i, j的最多路径数。
# 初始化：对于第一行 dp[0][j]，或者第一列 dp[i][0]，都只有一条路径。
# 机器人到达位置(i, j)有两种方式：从(i - 1, j)下移和从(i, j - 1)右移。状态转移方程为：
# dp[i][j]=dp[i−1][j]+dp[i][j−1]
# 复杂度分析
# 时间复杂度：O(mn)。遍历dp数组进行动态规划。
# 空间复杂度：O(mn)。创建的dp数组的大小。
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[i][j]



# 优化动态规划
# 可以只用一个滚动一维数组，上面的方法当前位置结果等于左边一个的结果加上上方的结果，在这个优化算法里，直接用dp[i] = dp[i - 1] + dp[i]来简化。这时右边的dp[i]的值相当于上方的结果。
# 时间复杂度：O(mn)。
# 空间复杂度：O(min(m, n))。
# 这里要注意j是从1到n，不能从0开始，第0位永远是1，不能被修改。建数组时除第一位外都要是0，不然第一轮1到n时，dp[i] = dp[i - 1] + dp[i]，本身也加进去了，会导致结果变大。
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        dp = [0] * n
        dp[0] = 1
        for i in range(m):
            for j in range(1, n):
                dp[j] = dp[j - 1] + dp[j]
        return dp[-1]


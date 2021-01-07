# There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color, and you need to cost the least. Return the minimum cost.
#
# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.
#
# Example
# Example 1:
#
# Input: [[14,2,11],[11,14,5],[14,3,10]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. Minimum cost: 2 + 5 + 3 = 10.
# Example 2:
#
# Input: [[1,2,3],[1,4,6]]
# Output: 3


#序列型动态规划
#算法：动态规划(dp)
# 算法思路
# dp[i][j]表示第i幢房子涂j的颜色最小的花费总和，即从前一幢房子的状态dp[i-1][k] (k != j)中选一个不同颜色且最小的再加上给第i幢房子涂j颜色的costs。
# 代码思路
# 初始化状态dp[0][i]=costs[0][i]
#
# 从左往右遍历每一幢房子，计算到该幢房子涂每种颜色的最小花费，状态转移方程是dp[i][j] = min{dp[i-1][k] +costs[i][j]} (k != j)
#
# 答案为到最后一幢房子涂每种颜色花费中的最小值，即min(dp[n-1][k]),k=0,1,2
#
# 复杂度分析
# N表示房子的幢数，即costs数组长度
#
# 空间复杂度：O(N)
# 时间复杂度：O(N)
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        if costs is None:
            return 0
        n = len(costs)
        dp = [[0, 0, 0] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(3):
                for k in range(3):
                    if j != k:
                        if dp[i][j] == 0:
                            dp[i][j] = dp[i - 1][k] + costs[i - 1][j]
                        else:
                            dp[i][j] = min(dp[i][j], dp[i - 1][k] + costs[i - 1][j])
        return min(dp[n][0], dp[n][1], dp[n][2])



#动态规划优化1，滚动数组，空间复杂度变成O(1)，优化2，直接在costs数组上操作，空间复杂度为0.待扩展
# 参考链接：https://www.jiuzhang.com/problem/paint-house/


#另一种动态规划思维，待理解：
# class Solution:
#
#     def minCost(self, costs) -> int:
#         r, b, g = 0, 0, 0
#         for r_c, b_c, g_c in costs:
#             r, b, g = r_c + min(b, g), b_c + min(r, g), g_c + min(r, b)
#         return min(r, b, g)



if __name__ == '__main__':
    input = [[14,2,11],[11,14,5],[14,3,10]]
    ref = Solution()
    output = ref.minCost(input)
    print(output)

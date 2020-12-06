# Determine if you are able to reach the last index.
# The array A contains 𝑛 integers 𝑎1, 𝑎2, …, 𝑎𝑛 (1≤𝑎𝑖≤5000) (1≤n≤5000 )
# Have you met this question in a real interview?
# Example
# Example 1
#
# Input : [2,3,1,1,4]
# Output : true
# Example 2
#
# Input : [3,2,1,0,4]
# Output : false
# Challenge
# This problem have two method which is Greedy and Dynamic Programming.
# The time complexity of Greedy method is O(n).
# The time complexity of Dynamic Programming method is O(n^2).
# We manually set the small data set to allow you pass the test in both ways. This is just to let you learn how to use this problem in dynamic programming ways. If you finish it in dynamic programming ways, you can try greedy method to make it accept again.


# 动态规划
# 解题思路
# 我们可以把该问题拆分成子问题，从前到后确定每个位置是否可达，用动态规划的思想求解。
# 建立dp数组，dp[i]表示能否跳到i位。
# 状态转移关系：
# 如果存在某点j，dp[j]为true且从j可以跳到i，那么dp[i]为true,否则，dp[i]为false
# 复杂度分析
# 时间复杂度：O(n2)，n为数组长度。双重遍历。
# 空间复杂度：O(n)，n为数组长度。建立的dp[]长度为n。
# 可行优化
# 提供一些优化的思路，大家有兴趣可以自行实现：
# 内层遍历改成从后向前，会比从前向后更节省时间。
# 仔细想想不难发现：如果可以跳到i点，则说明一定可以跳到i前面的任意一点。所以，如果i位为True，前面的位置一定是True。那么我们就无需开dp数组了，这样空间复杂度可以降到O(1)。
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        if A is None:
            return False
        n = len(A)
        dp = [True] + [False] * (n - 1)
        for i in range(1, n):
            for j in range(i):
                if dp[j] and j + A[j] >= i:
                    dp[i] = True
                    break
        return dp[-1]

# 动态规划优化1：内层遍历改成从后向前，会比从前向后更节省时间。



# 动态规划优化2：仔细想想不难发现：如果可以跳到i点，则说明一定可以跳到i前面的任意一点。所以，如果i位为True，前面的位置一定是True。那么我们就无需开dp数组了，这样空间复杂度可以降到O(1)。
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        if A is None:
            return False
        n = len(A)
        for i in range(1, n):
            for j in range(i):
                status = False
                if j + A[j] >= i:
                    status = True
                    break
            if status == False:
                return False
        return True



# 贪心法，最远可达距离＝当前index+当前value，动态更新farthest变量，如果farthest>=最后一个index，最返回true,如果当前index>farthest，则返回false
# 时间复杂度：O(n)
# 空间复杂度: O(1)
# 注意最后返回的是farthest >= n - 1，不是>= n。
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        if A is None or n == 0:
            return False
        n = len(A)
        farthest = 0
        for i in range(1, n):
            if farthest < i:
                return False
            else:
                farthest = max(farthest, i + A[i])
        return farthest >= n - 1

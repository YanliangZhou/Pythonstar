# Description
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
# It is guaranteed that the num of money will not exceed 10000.
# And the num of coins wii not exceed 500，The denomination of each coin will not exceed 100
#
# Have you met this question in a real interview?
# Example
# Example1
#
# Input:
# [1, 2, 5]
# 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example2
#
# Input:
# [2]
# 3
# Output: -1

import sys

class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        # write your code here
        n = len(coins)
        if amount == 0:
            return 0
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for k in coins:
                if i >= k and dp[i - k] != sys.maxsize:
                    dp[i] = min(dp[i], dp[i - k] + 1)
        if dp[amount] == sys.maxsize:
            return -1
        else:
            return dp[amount]

if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    solution = Solution()
    ans = solution.coinChange(coins, amount)
    print(ans)
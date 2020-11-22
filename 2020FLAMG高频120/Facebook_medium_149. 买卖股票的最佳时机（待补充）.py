# Description
# Given a string s and a dictionary of words dict, determine if s can be broken into a space-separated sequence of one or more dictionary words.
# Because of we have used stronger data, the ordinary DFS method can not pass this question now.
#
# s.length <= 1e5
# dict.size <= 1e5
#
# Have you met this question in a real interview?
# Example
# Example 1:
# 	Input:  "lintcode", ["lint", "code"]
# 	Output:  true
#
# Example 2:
# 	Input: "a", ["a"]
# 	Output:  true

# 算法：贪心
# 很容易想到的贪心算法。对于每一天的价格，我考虑在那天之前的最低价买入，看看是不是能跟新答案。
# 我们利用一个单元去保存前缀最小值，或者后缀最大值。以下以前缀最小值 low 为例。
# 若当前的 prices[i]−low 能更新答案，则更新。low=min(prices[i],low)，继续跟新最小值即可。
# 复杂度分析
# 时间复杂度 O(n)，空间复杂度 O(1)
class Solution:
	"""
	@param prices: Given an integer array
	@return: Maximum profit
	"""
	def maxProfit(self, prices):
		# write your code here
		if not prices:
			return 0
		low = prices[0]
		high = 0
		n = len(prices)
		for i in range(1, n):
			if prices[i] - low > high:
				high = prices[i] - low
			if prices[i] < low:
				low = prices[i]
		return high

# 可用动态规划解决，待做

if __name__ == '__main__':
	input = [4, 5, 1, 2, 3]
	solution = Solution()
	answer = solution.maxProfit(input)
	print(answer)

# Description
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# It is guaranteed that the length of nums doesn't exceed 20000
# The product of the largest subsequence of the product, less than 2147483647
#
# Have you met this question in a real interview?
# Example
# Example 1:
#
# Input:[2,3,-2,4]
# Output:6
# Example 2:
#
# Input:[-1,2,4,1]
# Output:8

# 动态规划
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        n = len(nums)
        f = [0] * n
        g = [0] * n
        f[0] = g[0] = nums[0]
        maxvalue = nums[0]
        for i in range(1, n):
            if nums[i] >= 0:
                f[i] = max(nums[i], nums[i] * f[i - 1])
                g[i] = min(nums[i], nums[i] * g[i - 1])
            if nums[i] <= 0:
                f[i] = max(nums[i], nums[i] * g[i - 1])
                g[i] = min(nums[i], nums[i] * f[i - 1])
            maxvalue = max(f[i], maxvalue)
        return maxvalue

# 另一种写法可以省去两个if,也就是不管当前位置是正是负，只取当前位置和前一位的最大最小值乘积的最大值和最小值：
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        n = len(nums)
        f = [0] * n
        g = [0] * n
        f[0] = g[0] = nums[0]
        maxvalue = nums[0]
        for i in range(1, n):
            f[i] = max(nums[i], max(nums[i] * f[i - 1], nums[i] * g[i - 1]))
            g[i] = min(nums[i], min(nums[i] * f[i - 1], nums[i] * g[i - 1]))
            maxvalue = max(maxvalue, f[i])
        return maxvalue




# 动态规划优化
# 【优化思路】 观察发现max_arri 和 min_arri至于前一状态max_arri - 1和 min_arri - 1有关，所以没有必要使用数组来保存状态，可以简化为状态变量，空间上可以减少一个维度。
# 空间复杂度：O(1)
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        n = len(nums)
        max_v = min_v = maxvalue =  nums[0]
        for i in range(1, n):
            cur_max, cur_min = max_v, min_v
            max_v = max(nums[i], max(nums[i] * cur_max, nums[i] * cur_min))
            min_v = min(nums[i], min(nums[i] * cur_max, nums[i] * cur_min))
            maxvalue = max(maxvalue, max_v)
        return maxvalue




if __name__ == '__main__':
    input = [-4,-3,-2]
    ref = Solution()
    output = ref.maxProduct(input)
    print(output)

# Description
# Given an array of integers, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are zero-based.
#
# You may assume that each input would have exactly one solution
#
# Have you met this question in a real interview?
# Example
# Example1:
# numbers=[2, 7, 11, 15], target=9
# return [0, 1]
# Example2:
# numbers=[15, 2, 7, 11], target=9
# return [1, 2]
# Challenge
# Either of the following solutions are acceptable:
#
# O(n) Space, O(nlogn) Time
# O(n) Space, O(n) Time
# Related Problems


class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        if len(number) == 0:
            return [-1, -1]

        num = [(number, index) for index, number in enumerate(numbers)]
        num = sorted(num)
        left, right = 0, len(num) -1
        while left < right:
            if num[left][0] + num[right][0] < target:
                left += 1
            elif num[left][0] + num[right][0] > target:
                right -= 1
            else:
                return sorted[num[left][1], num[right][1]]
        return [-1, -1]

# 使用双指针算法，时间复杂度 (nlogn)，空间复杂度 O(n)
# 优化： 算法：hashmap
# 用map记录所有当前查找过的num[i]，存下target-num[i]
#
# 如果存在num[j]在map中说明存在一对i,j的使得num[i],num[j]和为target，
#
# 即找到了答案
#
# 复杂度分析
# 时间复杂度O(n)
# n为数组的大小
# 空间复杂度O(n)
# n为数组的大小
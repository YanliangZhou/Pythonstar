# Description
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Have you met this question in a real interview?
# Example
# Example 1:
#
# Input: [4, 5, 1, 2, 3] and target=1,
# Output: 2.
# Example 2:
#
# Input: [4, 5, 1, 2, 3] and target=0,
# Output: -1.
# Challenge
# O(logN) time


# 用两次二分的方法。
# 第一次二分：找到最小数的位置，参考 find minimum number in rotated sorted array 第二次二分：确定 target 在左侧区间还是右侧，用一个普通的二分法即可找到。
# 时间复杂度O(logn)，实际是O(2*logn)
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return -1
        index = self.findmin(A)
        if A[index] <= target <= A[-1]:
            return self.binary_search(A, index, len(A) - 1, target)
        else:
            return self.binary_search(A, 0, index - 1, target)

    def findmin(self, A):
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] < A[left]:
                right = mid
            else:
                left = mid
        if A[left] > A[right]:
            return right
        return left

    def binary_search(self, A, left, right, target):
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] < target:
                left = mid
            else:
                right = mid
        if A[left] == target:
            return left
        if A[right] == target:
            return right
        return -1


# 用一次二分的方法
# 二分搜索时每次都是把数组分成两部分，先判段哪一部分是有序的
# 如果target在有序的那一部分，那么继续二分
# 如果在无序的那一部分，重复第一步
# 空间复杂度：O(N)
# 时间复杂度：O(logN)
# 中间的两次双边范围判定不需要等于A[mid]
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return -1
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] < A[left]:
                if A[mid] < target <= A[right]:
                    left = mid
                else:
                    right = mid
            else:
                if A[left] <= target < A[mid]:
                    right = mid
                else:
                    left = mid
        if A[left] == target:
            return left
        if A[right] == target:
            return right
        return -1





if __name__ == '__main__':
    input = [4, 5, 1, 2, 3]
    target = 1
    solution = Solution()
    answer = solution.search(input, target)
    print(answer)
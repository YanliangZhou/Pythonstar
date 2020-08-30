# Description
# Implement int sqrt(int x).
#
# Compute and return the square root of x.
#
# Have you met this question in a real interview?
# Example
# Example 1:
# Input: 0
# Output: 0
#
# Example 2:
# Input: 3
# Output: 1
#
# Explanation:
# return the largest integer y that y * y <= x.
#
# Example 3:
# Input: 4
# Output: 2
#
# Challenge
# O(log(x))

# 暴力遍历：
# class Solution:
#     """
#     @param x: An integer
#     @return: The sqrt of x
#     """
#     def sqrt(self, x):
#         # write your code here
#         i = 0
#         while i**2 <= x:
#             if (i+1)**2 > x:
#                 return i
#             else:
#                 i += 1
#
# if __name__ == '__main__':
#     s = Solution()
#     print(s.sqrt(0))


#二分法达到最佳时间复杂度O(logn)
class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        left, right = 0, x
        while left + 1 < right:
            mid = (left + (right - left) // 2)
            if mid ** 2 > x:
                right = mid
            elif mid ** 2 < x:
                left = mid
            else:
                return mid
        if right ** 2 == x:
            return right
        return left

if __name__ == '__main__':
     s = Solution()
     print(s.sqrt(1))
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

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        i = 0
        while i*2 <= x and (i+1)*2 > x:
            return i

if __name__ == '__main__':
    s = Solution()
    print(s.sqrt(1))
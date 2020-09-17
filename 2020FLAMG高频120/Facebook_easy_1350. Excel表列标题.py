# Description
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# 1 -> A
# 2 -> B
# 3 -> C
#  ...
# 26 -> Z
# 27 -> AA
# 28 -> AB
# Have you met this question in a real interview?
# Example
# Example1
#
# Input: 28
# Output: "AB"
# Example2
#
# Input: 29
# Output: "AC"

class Solution:
    """
    @param n: a integer
    @return: return a string
    """
    def convertToTitle(self, n):
        # write your code here
        output = []
        capitals = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        while n > 0:
            output.append(capitals[(n - 1) % 26])
            n = (n - 1) // 26
        output.reverse()
        return ''.join(output)


# 递归
class Solution:
    """
    @param n: a integer
    @return: return a string
    """
    def convertToTitle(self, n):
        # write your code here
        return '' if n <= 0 else self.convertToTitle((n - 1) // 26) + chr((n - 1) % 26 + ord('A'))

if __name__ == '__main__':
    input = 999
    solution = Solution()
    answer = solution.convertToTitle(input)
    print(answer)

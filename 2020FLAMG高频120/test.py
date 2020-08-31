class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        dic = {"[": "]", "{": "}", "(": ")"}
        stack = []
        for item in s:
            if item in dic:
                stack.append(dic[item])
            elif not stack or item != stack.pop():
                return False
        return not stack
#
if __name__ == '__main__':
    a = '([])'
    b = Solution()
    output = b.isValidParentheses(a)
    print(output)
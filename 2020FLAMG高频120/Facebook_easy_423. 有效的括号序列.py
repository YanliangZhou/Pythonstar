# Description
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
#
# Have you met this question in a real interview?
# Example
# Example 1:
#
# Input: "([)]"
# Output: False
# Example 2:
#
# Input: "()[]{}"
# Output: True
# Challenge
# Use O(n) time, n is the number of parentheses.

class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        stack = []
        for item in s:
            if item == '[' or item == '(' or item == '{':
                stack.append(item)
            else:
                if not stack:
                    return False
                elif item == ']' and stack[-1] == '[' or item == ')' and stack[-1] == '(' or item == '}' and stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return False
        return not stack


#另一种利用栈和字典的更简洁写法，但是需要多花一个字典空间
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
# Description
# For a given source string and a target string, you should output the first index(from 0) of target string in source string.
#
# If target does not exist in source, just return -1.
#
# Have you met this question in a real interview?
# Clarification
# Do I need to implement KMP Algorithm in a real interview?
#
# Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your basic implementation ability. But make sure you confirm with the interviewer first.
# Example
# Example 1:
#
# Input: source = "source" ，target = "target"
# Output: -1
# Explanation: If the source does not contain the target content, return - 1.
# Example 2:
#
# Input:source = "abcdabcdefg" ，target = "bcd"
# Output: 1
# Explanation: If the source contains the target content, return the location where the target first appeared in the source.
# Challenge
# O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)
#
# Related Problems
# 594.strStr II

class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        sourcelen = len(source)
        targetlen = len(target)
        if targetlen == 0:
            return 0
        if targetlen > sourcelen:
            return -1
        k = i
        for i in range(sourcelen - targetlen + 1):
            for j in range(targetlen):
                if source[k] == target[j]:
                    if j == targetlen-1:
                        return i
                    k+=1
                else:
                    break
        return -1

# M表示 source 的长度
# N表示 target 的长度
# 空间复杂度：O(M+N)
# 时间复杂度：O(MN)
# 优化：可用KMP算法实现O(N)
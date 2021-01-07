# Description
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
# we can't decode an empty string. So you should return 0 if the message is empty.
# The length of message n≤100
#
# Example
# Example 1:
# Input: "12"
# Output: 2
# Explanation: It could be decoded as AB (1 2) or L (12).
#
# Example 2:
# Input: "10"
# Output: 1

#划分型动态规划
#如果最后一位是0，那么只会是10，不会是最后一位单个解码的情况。如果最后两位大于26，那么只可能是最后一位单独解码。总结码方法数量等于最后一位单独解码的量加上最后两位一起解码的量。需要注意第一位是0的话，也返回0。这里的输入是string，不能直接当数字来操作，需要转化成数字。这里if s == '' or s[0] == '0':顺序不能变，因为如果=0在前面，s=''时会报错out of range。这里dp[0]初始值不能照直觉是0，不然loop里面会变复杂。
# 复杂度分析：
# N表示字符串长度
# 空间复杂度： O(n)
# 时间复杂度： O(n)
class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        if s == '' or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            if int(s[i - 1]) >= 1 and int(s[i - 1]) <= 9:
                dp[i] = dp[i - 1]
            if i > 1:
                j = 10 * int(s[i - 2]) + int(s[i - 1])
                if 10 <= j <= 26:
                    dp[i] += dp[i - 2]
        return dp[n]

#可用滚动数组优化


if __name__ == '__main__':
    input = ""
    ref = Solution()
    output = ref.numDecodings(input)
    print(output)

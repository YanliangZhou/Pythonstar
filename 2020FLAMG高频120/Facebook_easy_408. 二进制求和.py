# Description
# Given two binary strings, return their sum (also a binary string).
#
# Have you met this question in a real interview?
# Example
# Example 1:
#
# Input:
# a = "0", b = "0"
# Output:
# "0"
# Example 2:
#
# Input:
# a = "11", b = "1"
# Output:
# "100"

# 莽夫算法，变成整形一位一位加，考虑所有情况，疯狂出bug
class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """
    def addBinary(self, a, b):
        # write your code here
        a = list(a)
        b = list(b)
        left, right = len(a) - 1, len(b) - 1
        plus = 0
        if left >= right:
            a.insert(0, 0)
            left += 1
            while left >= 0:
                while right >= 0:
                    if int(a[left]) + int(b[right]) + plus >= 2:
                        a[left] = int(a[left]) + int(b[right]) + plus - 2
                        plus = 1
                        left -= 1
                        right -= 1
                    else:
                        a[left] = int(a[left]) + int(b[right]) + plus
                        plus = 0
                        left -= 1
                        right -= 1
                if plus == 1:
                    if int(a[left]) + plus == 2:
                        a[left] = 0
                        plus = 1
                        left -= 1
                    else:
                        a[left] = int(a[left]) + plus
                        a = list(map(str, a))
                        a = "".join(a)
                        a = int(a)
                        a = str(a)
                        return a
                else:
                    a = list(map(str, a))
                    a = "".join(a)
                    a = int(a)
                    a = str(a)
                    return a
            a = list(map(str, a))
            a = "".join(a)
            a = int(a)
            a = str(a)
            return a
        else:
            b.insert(0, 0)
            right += 1
            while right >= 0:
                while left >= 0:
                    if int(a[left]) + int(b[right]) + plus >= 2:
                        b[right] = int(a[left]) + int(b[right]) + plus - 2
                        plus = 1
                        left -= 1
                        right -= 1
                    else:
                        b[right] = int(a[left]) + int(b[right]) + plus
                        plus = 0
                        left -= 1
                        right -= 1
                if plus == 1:
                    if int(b[right]) + plus == 2:
                        b[right] = 0
                        plus = 1
                        right -= 1
                    else:
                        b[right] = int(b[right]) + plus
                        b = list(map(str, b))
                        b = "".join(b)
                        b = int(b)
                        b = str(b)
                        return b
                else:
                    b = list(map(str, b))
                    b = "".join(b)
                    b = int(b)
                    b = str(b)
                    return b
            b = list(map(str, b))
            b = "".join(b)
            b = int(b)
            b = str(b)
            return b


#直接用int()和bin()转换，简单，但不能达到考察目的
class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """
    def addBinary(self, a, b):
        # write your code here
        a = int(a, 2)
        b = int(b, 2)
        sum = str(bin(a + b))
        return sum[2: len(sum)]


#官方办法，类似于第一种，不过很巧妙地省去了很多if判断
class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """
    def addBinary(self, a, b):
        # write your code here
        indexa = len(a) - 1
        indexb = len(b) - 1
        plus = 0
        sum = ""
        while indexa >= 0 or indexb >= 0:
            x = int(a[indexa]) if indexa >= 0 else 0
            y = int(b[indexb]) if indexb >= 0 else 0
            if (x + y + plus) % 2 == 0:
                sum = '0' + sum
            else:
                sum = '1' + sum
            plus = (x + y + plus) // 2
            indexa, indexb = indexa - 1, indexb - 1
        if plus == 1:
            sum = '1' + sum
        return sum


if __name__ == '__main__':
    a = '11'
    b = '11'
    s = Solution()
    print(s.addBinary(a, b))
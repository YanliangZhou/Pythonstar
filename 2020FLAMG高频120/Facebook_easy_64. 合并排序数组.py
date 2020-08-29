# Description
# Given two sorted integer arrays A and B, merge B into A as one sorted array.
#
# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
#
# Have you met this question in a real interview?
# Example
# Example 1:
#
# Input：[1, 2, 3] 3  [4,5]  2
# Output：[1,2,3,4,5]
# Explanation:
# After merge, A will be filled as [1, 2, 3, 4, 5]
# Example 2:
#
# Input：[1,2,5] 3 [3,4] 2
# Output：[1,2,3,4,5]
# Explanation:
# After merge, A will be filled as [1, 2, 3, 4, 5]

class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        left, right = m - 1, n - 1
        index = m + n - 1
        while left >= 0 and right >= 0:
            if A[left] >= B[right]:
                A[index] = A[left]
                left -= 1
                index -= 1
            else:
                A[index] = B[right]
                right -= 1
                index -= 1
        while left >= 0:
            A[index] = A[left]
            left -= 1
            index -= 1
        while right >= 0:
            A[index] = B[right]
            right -= 1
            index -= 1


# 复杂度
# 时间复杂度：O(n+m)，n,m分别为A,B数组的元素个数
# 利用双指针各自遍历一遍对应的数组；
# 空间复杂度：O(1)
# 只需要新建pointA,pointB和index三个整型变量；
# 精简代码：可以用--来表示赋值并让变量减一
# int pos = m + n - 1 , i = m - 1 , j = n - 1;
#         while (i >= 0 && j >= 0)
#             A[pos--] = A[i] > B[j] ? A[i--] : B[j--];
#         while (i >= 0)
#             A[pos--] = A[i--];
#         while (j >= 0)
#             A[pos--] = B[j--];
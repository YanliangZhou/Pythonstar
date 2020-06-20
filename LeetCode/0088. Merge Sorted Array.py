class Solution:
    def merge(self, nums1, m, nums2, n):
        while n > 0:
            if m <= 0 or nums2[n-1] >= nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1

if __name__ == "__main__":
    nums1 = [2, 4, 0]
    nums2 = [1]
    Merge = Solution()
    result = Merge.merge(nums1,2,nums2,1)
    print(nums1)
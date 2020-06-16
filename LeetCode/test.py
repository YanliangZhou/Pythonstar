class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != val :
                nums[count] = nums[i]
                count +=1
        return count

if __name__ == "__main__":
    nums = [4, 4, 7, 6, 6, 4]
    solution = Solution()
    output = solution.removeElement(nums, 4)
    # print(output)
    # print(nums)

A = [4, -4, 7, -6, 6, 4]
# for x in range(1, len(A) + 1):
#     # print(x)
print(A[0, 2])
# Description
# Given a sorted array, 'remove' the duplicates in place such that each element appear only once and return the 'new' length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# Have you met this question in a real interview?
# Example
# Example 1:
#
# Input:  []
# Output: 0
# Example 2:
#
# Input:  [1,1,2]
# Output: 2
# Explanation:  uniqued array: [1,2]

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        i = 0
        while i < len(nums):
            if i == len(nums) - 1:
                break
            elif nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1
        return len(nums)

if __name__ == '__main__':
    a = [3,10,10,16,22]
    s = Solution()
    s.removeDuplicates(a)
    print(s)
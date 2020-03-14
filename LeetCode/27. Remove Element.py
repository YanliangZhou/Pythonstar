
class Solution:
    def removeElement(self, nums, val):
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start += 1
        return start

if __name__ == "__main__":
    nums = [4, 4, 7, 6, 6, 4]
    solution = Solution()
    output = solution.removeElement(nums, 4)
    print(output)
    print(nums)
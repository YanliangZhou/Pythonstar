class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i +=1
                nums[i] = nums[j]
        return i + 1

if __name__ == "__main__":
    list = [1, 1, 1, 2, 2, 3, 4, 4, 5]
    solution = Solution()
    output = solution.removeDuplicates(list)
    print(output)
    print(list)
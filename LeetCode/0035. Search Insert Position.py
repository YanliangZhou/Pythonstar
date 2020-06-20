class Solution:
    def searchInsert(self, nums, target):
        first , last = 0, len(nums)-1
        while first <= last:
            mid=(first+last)//2
            if nums[mid]== target:
                return mid
            if nums[mid] < target:
                first = mid+1
            else:
                last = mid-1
        return first

if __name__ == "__main__":
    nums = [1, 2, 4, 6, 8, 9]
    solution = Solution()
    output = solution.searchInsert(nums, 7)
    print(output)
    print(nums)
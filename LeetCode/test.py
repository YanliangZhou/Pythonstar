# class Solution:
#     def twoSum(self, nums, target):
#        diction = {}
#        count = 0
#        for i in range(len(nums)):
#            if nums[i] in diction.keys() and 2*nums[i] == target:
#                return [diction[nums[i]], count]
#            diction[nums[i]] = i
#            remain = target - nums[i]
#            count += 1
#            if remain in diction.keys() and diction[remain] != diction[nums[i]]:
#                if diction[remain] < diction[nums[i]]:
#                     return [diction[remain], i]
#                else:
#                     return [i, diction[remain]]
#
# if __name__ == "__main__":
#     list = [3, 3]
#     answer = Solution()
#     sol = answer.twoSum(list, 6)
#     print(sol)




print(3.8//2)
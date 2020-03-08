# class Solution(object):
#     def twoSum(self, nums, target):
#         if len(nums) <= 1:
#             return False
#         buff_dict = {}
#         for i in range(len(nums)):
#             if nums[i] in buff_dict:
#                 return [buff_dict[nums[i]], i]
#             else:
#                 buff_dict[target - nums[i]] = i

def twoSum(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        remaining = target - v
        if remaining in seen:
            return [seen[remaining], i]
        seen[v] = i
    return []
if __name__ == "__main__":
    a = [4,5,7,6,2,9]
    s = []
    s.append(twoSum(a,11))
    print(s)
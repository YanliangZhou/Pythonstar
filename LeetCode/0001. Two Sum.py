class Solution():
    def twoSum(delf, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            else:
                seen[v] = i
        return []

if __name__ == "__main__":
    a = [4, 5, 7, 6, 2, 9]
    solution = Solution()
    s = []
    s.append(solution.twoSum(a,11))
    print(s)

# extention：How to code if there exist more than one case that match the target?
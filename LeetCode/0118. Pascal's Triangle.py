class Solution:
    def generate(self, numRows):
        if numRows > 0:
            res = [[1]]
            for i in range(1, numRows):
                res += [list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))]
            return res
        else:
            return []
# 需要考虑 numRows = 0的情况
if __name__ == "__main__":
    gen = Solution()
    Gen = gen.generate(5)
for i in range(len(Gen)):
    print(Gen[i])
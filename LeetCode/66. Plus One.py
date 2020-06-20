class Solution:
    def plusOne(self, digits):
        results = list(map(str, digits))
        results1 = map(str, digits)
        num = ''.join(results)
        Num = int(num)+1
        resultlist = [int(x) for x in str(Num)]
        print(results1)
        return resultlist

if __name__ == "__main__":
    digits = [4,3,2,9]
    Plus = Solution()
    plusone = Plus.plusOne(digits)
    print(plusone)

def maxProfit(prices):
        # write your code here
        total = 0
        low, high = sys.maxint, 0
        for x in prices:
            if x - low > total:
                total = x - low
            if x < low:
                low = x
        return total

prices = [3, 2, 3, 1, 2]
print(maxProfit(prices))

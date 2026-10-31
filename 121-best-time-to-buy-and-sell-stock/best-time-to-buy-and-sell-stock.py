class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = prices[0]
        maxprofit = 0

        for price in prices:
            if price < lowest:
                lowest = price

            todayprofit = price - lowest
            maxprofit = max(maxprofit, todayprofit)

        return maxprofit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        cheap = prices[0]
        for i in range(len(prices)):
            if cheap >  prices[i]:
                cheap =  prices[i]
            if  prices[i] - cheap > best:
                best =  prices[i] - cheap
        return best
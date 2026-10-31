class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest=prices[0]
        maxprofit=0
        for i in range(len(prices)):
            if(lowest > prices[i]):
                lowest=prices[i]

            todayprofit=prices[i]-lowest

            if( todayprofit > maxprofit):
                maxprofit=todayprofit
            
        return maxprofit
   
                
        return profit
        
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best=0
        cheap=prices[0]
        for i in range(0,len(prices)):
            current=prices[i]
            if(cheap>current):
                cheap=current
            if(current-cheap>best):
                best=current-cheap
        return(best)
            


        
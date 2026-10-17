class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp=[amount+1] * (amount+1)
        dp[0]=0

        for i in range(1,amount+1):
            for c in coins:
                if c <= i:
                    dp[i]=min(dp[i],1+dp[i-c])
        
        if(dp[amount] != amount+1):
            return dp[amount]
        else:
            return -1



        
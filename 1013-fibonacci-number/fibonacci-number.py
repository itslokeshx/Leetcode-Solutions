class Solution:
    def fib(self, n: int) -> int:
        dp=[-1]*(n+1)
        def memo(n):
            if(n==0):
                return 0
            if(n<=1):
                return 1
            if(dp[n]!=-1):
                return dp[n]
            ans=memo(n-1)+memo(n-2)
            dp[n]=ans
            return ans
        return memo(n)
        


        
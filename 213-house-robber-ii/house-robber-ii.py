class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def robarray(dparray):
            if len(dparray)==1:
                return dparray[0]
            dp =[0]*len(dparray)
            dp[0] = dparray[0]
            dp[1] = max(dparray[0],dparray[1])
            for i in range(2, len(dparray)):
                dp[i]=max(dp[i-1],dp[i-2]+dparray[i])
            return dp[-1]
        return max( robarray(nums[1:]), robarray(nums[:-1]) )
class Solution:
    def rob(self, nums: list[int]) -> int:
        dp=[0]*len(nums)
        if(len(nums)==1):
            return nums[0]
        dp[0]=nums[0]
        best=0
        for i in range(1,len(nums)):
            best=max(dp[i-1], dp[i-2]+nums[i])
            dp[i]=best
        return best
           
        
        


        
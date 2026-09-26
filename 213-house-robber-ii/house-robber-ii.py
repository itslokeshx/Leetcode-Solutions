class Solution:
    def rob(self, nums: list[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        dparray1=nums[1:]
        dparray2=nums[:-1]
        dp1=[0]*len(dparray1)
        dp1[0]=dparray1[0]
        for i in range(1,len(dparray1)):
            dp1[i]=max(dp1[i-1],dp1[i-2]+dparray1[i])
        dp2=[0]*len(dparray2)
        dp2[0]=dparray2[0]
        for i in range(1,len(dparray2)):
            dp2[i]=max(dp2[i-1],dp2[i-2]+dparray2[i])
        return max(dp1[-1],dp2[-1])

        
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmin=nums[0]
        cmax=nums[0]
        best=nums[0]
    
        for i in range(1,len(nums)):
            tempmin=nums[i]*cmin
            tempmax=nums[i]*cmax
            cmin=min(tempmin,nums[i],tempmax)
            cmax=max(nums[i],tempmax,tempmin)
            if(cmax>best):
                best=cmax
        return best

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sums=[0]*len(nums)
        runningsums=0
        for i in range(len(nums)):
            runningsums+=nums[i]
            sums[i]=runningsums
        return sums
    

        
        
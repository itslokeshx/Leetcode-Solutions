class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix=len(nums)*[0]
        for i in range(0,len(nums)):
            prefix[i]=nums[i]+prefix[i-1]
        return(prefix)
        
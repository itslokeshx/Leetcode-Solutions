class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix=len(nums)*[0]
        for i in range(0,len(nums)):
            if(i==0):
                 prefix[i]=nums[i]
            else:
                prefix[i]=nums[i]+prefix[i-1]
        return(prefix)
        
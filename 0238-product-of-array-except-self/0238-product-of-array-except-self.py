class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=len(nums)*[0]
        suffix=len(nums)*[0]
        final=len(nums)*[0]

        for i in range(0,len(nums)):
            if(i==0):
                prefix[i]=1
            else:
                prefix[i]=nums[i-1]*prefix[i-1]
        for i in range(len(nums)-1,-1,-1):
            if(i==len(nums)-1):
                suffix[i]=1
            else:
                suffix[i]=nums[i+1]*suffix[i+1]
        for i in range(0,len(nums)):
            final[i]=prefix[i]*suffix[i]
        return final
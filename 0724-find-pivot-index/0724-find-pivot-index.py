class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=len(nums)*[0]
        suffix=len(nums)*[0]
        pivot=0
        for i in range(0,len(nums)):
            if(i==0):
                prefix[i]=0
            else:
                prefix[i]=nums[i-1]+prefix[i-1]
        for i in range(len(nums)-1,-1,-1):
            if(i==len(nums)-1):
                suffix[i]=0
            else:
                suffix[i]=nums[i+1]+suffix[i+1]
        for i in range(0,len(nums)):
            if(suffix[i]==prefix[i]):
                pivot=i
                break
            else:
                pivot=-1
        return pivot


        
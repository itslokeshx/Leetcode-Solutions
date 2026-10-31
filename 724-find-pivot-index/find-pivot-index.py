class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        prefix=[0] * len(nums)
        suffix=[0] * len(nums)

        for i in range(len(nums)):
            if(i==0):
                prefix[i]=nums[i]
            else:
                prefix[i]=prefix[i-1]+nums[i]

        for i in range(len(nums)-1,-1,-1):
            if(i== (len(nums)-1) ):
                suffix[i]=nums[i]
            else:
                suffix[i]=suffix[i+1]+nums[i]
        for i in range(len(nums)):
            if(prefix[i] == suffix[i]):
                return i
        return -1     
        
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ranges=[]
        start=0

        for i in range(1,len(nums)):
            if( nums[i] == nums[i-1] +1 ): 
                continue
            if(start == i-1):
                ranges.append(str(nums[start]))
            else:
                ranges.append(f"{(nums[start])}->{(nums[i-1])}" )
            start=i
        if nums:
            if(start == len(nums)-1):
                ranges.append(str(nums[start]))
            else:
                ranges.append(f"{nums[start]}->{nums[-1]}")
      
        return ranges






        
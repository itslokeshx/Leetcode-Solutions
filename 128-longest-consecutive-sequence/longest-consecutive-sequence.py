class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        if(not nums):
            return 0
        count=1
        longest=0
        for i in range(1,len(nums)):
            if(nums[i] == nums[i-1]+1):
                count+=1
            else:
                if(nums[i] == nums[i-1]):
                    continue
                longest=max(longest,count)
                count=1
        longest=max(longest,count)

        return longest

        
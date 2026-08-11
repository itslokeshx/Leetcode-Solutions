class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major=0
        seen={}
        for i in range(0,len(nums)):
            if(nums[i] not in seen):
                seen[nums[i]]=1
            else:
                seen[nums[i]]+=1
        for key,value in seen.items():
            if(value>=(len(nums)/2)):
                major=key
        return major
           

        
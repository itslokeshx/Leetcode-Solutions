class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashdict={}
        for i in range(len(nums)):
            dif=target-nums[i]
            if(dif in hashdict):
                return [hashdict[dif],i]
            else:
                hashdict[nums[i]]=i
        


        
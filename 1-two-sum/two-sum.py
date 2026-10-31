class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if(diff in hashmap):
                return([i,hashmap[diff]])
            else:
                hashmap[nums[i]]=i
        

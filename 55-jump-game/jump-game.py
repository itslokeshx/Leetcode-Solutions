class Solution:
    def canJump(self, nums: list[int]) -> bool:

        distance=0

        if(len(nums) == 1):
            return True

        for i in range(len(nums)):
            if( distance >= i):
                distance=max(distance, i + nums[i])
            if(distance >= len(nums)-1):
                return True
        return False
        
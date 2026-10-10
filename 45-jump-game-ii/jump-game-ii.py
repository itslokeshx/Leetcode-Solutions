class Solution:
    def jump(self, nums: list[int]) -> int:

        farthest=0
        jumps=0
        current_range=0
        if(len(nums) ==1):
            return 0
        for i in range(len(nums)-1):
            if( farthest >= i):
                farthest=max(farthest,i+nums[i])
                if(i == current_range):
                    jumps+=1
                    current_range=farthest
        return jumps
        
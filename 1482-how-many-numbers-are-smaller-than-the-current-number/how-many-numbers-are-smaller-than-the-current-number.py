class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        op=[]
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if( nums[i] > nums[j] ):
                    count+=1
            op.append(count)
            count=0
        return op
        
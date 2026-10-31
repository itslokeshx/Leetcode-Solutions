class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix=[0]*len(nums)
        for i in range(len(nums)):
            if(i==0):
                self.prefix[i]=nums[i]
            else:
                self.prefix[i]=self.prefix[i-1]+nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if(left==0):
            return self.prefix[right]
        return self.prefix[right]-self.prefix[left-1]
        
        

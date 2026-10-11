class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total=len(nums)
        spl_nums=[]
        squares=0
        for i in range(1,len(nums)+1):
            if( total % i == 0 ):
                spl_nums.append(i)
        for i in spl_nums:
            squares+= nums[i-1]**2
        return squares
    
        
                
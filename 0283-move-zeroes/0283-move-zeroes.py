class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow=0
        fast=0
        temps=0
        tempf=0
        for i in range(0,len(nums)):
            fast=i
            temps=nums[slow]
            tempf=nums[fast]
   
            if(nums[fast]!=0):
                nums[fast]=temps
                nums[slow]=tempf
                slow+=1
 
       
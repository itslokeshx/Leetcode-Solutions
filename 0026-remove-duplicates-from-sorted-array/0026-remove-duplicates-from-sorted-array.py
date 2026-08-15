class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow=0
        fast=0
        k=0
        for i in range(0,len(nums)):
            fast=i
            if(fast==0):
               slow+=1
               k+=1
               
            if(nums[slow-1]!=nums[fast]):
                nums[slow]=nums[fast]
                slow+=1
                k+=1
            elif(len(nums)==1):
                k=1
        return(k)


           
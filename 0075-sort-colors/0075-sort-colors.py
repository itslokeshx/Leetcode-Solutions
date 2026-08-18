class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        mid=0
        high=len(nums)-1
        tmplow=0
        tmpmid=0
        tmphigh=0
        while mid<=high:
            tmplow=nums[low]
            tmpmid=nums[mid]
            tmphigh=nums[high]
            if(nums[mid]==0):
                nums[low]=tmpmid
                nums[mid]=tmplow
                mid+=1
                low+=1
            elif(nums[mid]==1):
                mid+=1
            else:
                nums[mid]=tmphigh
                nums[high]=tmpmid
                high-=1
        



        
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        result=len(nums)*[0]
        pos=len(nums)-1
        leftnum=0
        rightnum=0
        while left<=right:
            rightnum=nums[right]*nums[right]
            leftnum=nums[left]*nums[left]
            if(leftnum<rightnum):
                result[pos]=rightnum
                right-=1
                pos-=1
            else:
                result[pos]=leftnum
                left+=1
                pos-=1
        return(result)



        
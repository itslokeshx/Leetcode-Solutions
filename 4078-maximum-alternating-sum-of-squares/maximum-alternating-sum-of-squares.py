class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        result=[0]*len(nums)

        for i in range(len(nums)):
            nums[i]=nums[i] ** 2

        nums.sort()

        eve=0
        odd=len(nums)-1

        for i in range(len(nums)):
            if(i%2==0):
                result[i]=nums[odd]
                odd-=1
            else:
                result[i]=nums[eve]
                eve+=1
        final=0
        for i in range(len(nums)):
            if(i%2==0):
                final+=result[i]
            else:
                final-=result[i]
        return final
  




        
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        result=0

        for i in range(len(nums)):
            nums[i]=nums[i] ** 2

        nums.sort()

        eve=0
        odd=len(nums)-1

        for i in range(len(nums)):
            if(i%2==0):
                result+=nums[odd]
                odd-=1
            else:
                result-=nums[eve]
                eve+=1

        return result
  
  




        
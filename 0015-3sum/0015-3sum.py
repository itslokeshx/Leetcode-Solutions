class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sumlist=[]
        nums.sort()


        for i in range(0,len(nums)):
            if( i>0 and nums[i]==nums[i-1]):
                continue
            left=i+1
            right=len(nums)-1
            
          
            
            while left<right:
                if(nums[i]+nums[left]+nums[right]==0):
                    sumlist.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[left]==nums[right+1]:
                        right-=1
                elif(nums[i]+nums[left]+nums[right]>0):
                    right-=1
                elif(nums[i]+nums[left]+nums[right]<0):
                    left+=1
        return(sumlist)

                


            
        
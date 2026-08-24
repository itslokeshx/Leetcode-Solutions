class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        current_sum=sum(nums[:k])
        max_sum=current_sum
        for right in range(k,len(nums)):
            current_sum-=nums[left]
            current_sum+=nums[right]
            max_sum=max(current_sum,max_sum)
            left+=1
        return max_sum/k


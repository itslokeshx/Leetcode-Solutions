class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        current_window_avg=0
        max_avg=float('-inf')
        for right in range(0,len(nums)):
            current_window_avg+=nums[right]
            if(right-left+1 == k):
                max_avg=max(current_window_avg,max_avg)
                current_window_avg-=nums[left]
                left+=1

        return max_avg/k

       
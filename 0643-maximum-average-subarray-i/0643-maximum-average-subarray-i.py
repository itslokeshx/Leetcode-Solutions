class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        init_value=sum(nums[:k])
        currentavg=(sum(nums[:k]))/k
        bestavg=(sum(nums[:k]))/k
        currentvalue=sum(nums[:k])
        for right in range(k,len(nums)):
            currentavg= currentvalue - nums[left]
            currentavg=currentavg+nums[right]
            currentvalue=currentavg
            currentavg=currentavg/k
            left+=1
            if(currentavg>bestavg):
                bestavg=currentavg
        return bestavg



        
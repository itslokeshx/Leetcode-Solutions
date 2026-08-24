class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left=0
        seen=set()
        flag=False
        for right in range(0,len(nums)):
            if(nums[right] in seen):
                return True
            seen.add(nums[right])
            if(right-left+1 >k):
                seen.remove(nums[left])
                left+=1
        return False

            
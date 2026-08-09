class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cp=0
        ans=0
        seen={}
        for i in range(0,len(nums)):
            if(cp not in seen):
                seen[cp]=1
            else:
                seen[cp]+=1
            cp+=nums[i]
            req=cp-k
            if(req in seen):
                ans+=seen[req]
        return ans
        
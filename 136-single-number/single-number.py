class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq={}
        for i in nums:
            if(i not in freq):
                freq[i]=1
            else:
                freq[i]+=1
        for key,value in freq.items():
            if(value==1):
                return key
        
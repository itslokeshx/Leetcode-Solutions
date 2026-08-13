class Solution:
    def longestPalindrome(self, s: str) -> int:
        mapping={}
        count=0
        flag=False
        for i in range(0,len(s)):
            if(s[i] not in mapping):
                mapping[s[i]]=1
            else:
                mapping[s[i]]+=1
        for value in mapping.values():
            count+=(value//2)*2
            if(value%2!=0):
                flag=True
        if(flag):
            count+=1
        return count
        
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        unique=-1
        for i in range(0,len(s)):
            if(s[i] not in count):
                count[s[i]]=1
               
            else:
                count[s[i]]+=1
        for key,value in count.items():
            if(value==1):
                unique=s.index(key)
                break
        return unique
        
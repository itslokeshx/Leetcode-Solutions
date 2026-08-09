class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sseen={}
        tseen={}
        for i in range(0,len(s)):
            if(s[i] not in sseen):
                sseen[s[i]]=1
            else:
                sseen[s[i]]+=1
        for i in range(0,len(t)):
            if(t[i] not in tseen):
                tseen[t[i]]=1
            else:
                tseen[t[i]]+=1
        return(sseen==tseen)
        

        
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappings={}
        flag=True
        for i in range(0,len(s)):
            if(s[i] not in mappings):
                if(t[i] in mappings.values()):
                    flag=False
                    break 
                mappings[s[i]]=t[i]
            else:
                if(mappings[s[i]]!=t[i]):
                    flag=False
                    break   
        return flag
                
        
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping={}
        flag=True
        for i in range(0,len(s)):
            if(s[i] not in mapping):
                if(t[i] in mapping.values()):
                    flag=False
                    break 
                mapping[s[i]]=t[i]
            else:
                if(mapping[s[i]]!=t[i]):
                    flag=False
                    break   
               

                else:
                    continue  
        return flag
                
        
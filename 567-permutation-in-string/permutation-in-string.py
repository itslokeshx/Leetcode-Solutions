class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        k=len(s1)-1
        flag=False
        s1="".join(sorted(s1))
        for right in range(k,len(s2)):
            window=s2[left:right+1]
            window_sorted="".join(sorted(window))
            if(window_sorted == s1):
                flag=True
            else:
                left+=1
        return flag
            
        
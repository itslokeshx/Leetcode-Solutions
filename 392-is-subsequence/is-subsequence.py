class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        spointer=0
        tpointer=0
        if( s == ""):
            return True
        for i in range(len(t)):
            if(s[spointer] == t[i]):
                spointer+=1
                tpointer+=1
            else:
                tpointer+=1
            if(spointer== len(s)):
                return True
        return False


        
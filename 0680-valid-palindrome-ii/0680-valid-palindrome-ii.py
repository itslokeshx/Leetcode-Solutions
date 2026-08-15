class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        flag=False
        def ispal(left,right):
            while left<right:
                if(s[left]==s[right]):
                    left+=1
                    right-=1
                else:
                    return False
            return True
        while left<right:
            if(s[left]==s[right]):
                left+=1
                right-=1
            else:
                return(ispal(left,right-1)or ispal(left+1,right))
        return True
                    
        
            

      
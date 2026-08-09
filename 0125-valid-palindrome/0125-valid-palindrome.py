class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=""
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()
        s=cleaned.lower()
        left=0
        right=len(s)-1
        pal=True
        while left < right:
            if(s[left]!=s[right]):
                pal=False
                break
            else:
                left+=1
                right-=1
                pal=True
        return pal
            
     

            
      
                
      
        
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars=""
        for i in s:
            if(i.isalnum()):
                chars+=i.lower()
        left=0
        right=len(chars)-1
        while(left < right):
            if(chars[left] == chars[right]):
                left+=1
                right-=1
            else:
                return False
        return True

        
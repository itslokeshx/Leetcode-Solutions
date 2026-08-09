class Solution:
    def isPalindrome(self, x: int) -> bool:
        string=str(x)
        reverse=""
        for i in range(len(string)-1,-1,-1):
            reverse+=string[i]
        if(reverse==string):
            return(True)
        else:
            return(False)

    
        
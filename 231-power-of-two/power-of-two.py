class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n==0 or n<0):
            return False
        while n!=0:
            n=n&(n-1)
            if(n>1):
                return False
        return True
            
        
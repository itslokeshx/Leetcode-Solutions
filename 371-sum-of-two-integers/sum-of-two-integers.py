class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask=0xFFFFFFFF
        max_int=0x7FFFFFFF
        
        xor = (a ^ b) & mask
        carry = ((a & b) << 1 )& mask
        
        while carry!=0:
            a=xor
            b=carry
            xor = (a ^ b) & mask
            carry = ((a & b) << 1) & mask

        if( xor > max_int):
            xor = ~(mask ^ xor)

        return xor
           
        

        
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        strnumb=""
        for i in digits:
            strnumb+=str(i)
        op=int(strnumb)+1
        strnumb=str(op)
        final=[]
        for i in strnumb:
            final.append(int(i))
        return final
        
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        count=0
        need=0
        for i in s:
            if(i == "("):
                stack.append("(")
                count+=1
            elif(i == ")"):
                if(stack):
                    stack.pop()
                    count-=1
                else:
                    need+=1
            
        return count+need

        
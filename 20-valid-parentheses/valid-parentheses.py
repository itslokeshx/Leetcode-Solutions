class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pair={
            "}":"{",
            ")":"(",
            "]":"["
        }
        for i in s:
            if(i in "{(["):
                stack.append(i)
            else:
                if(stack and pair[i] == stack[-1]):
                    stack.pop()
                else:
                    return False
        if(stack):
            return False
        else:
            return True
                
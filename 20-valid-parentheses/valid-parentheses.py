class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={
            "(":")",
            "{":"}",
            "[":"]",
            ")":"(",
            "}":"{",
            "]":"["
        }
        for char in s:
            if(char == "(" or char=="{" or char =="["):
                stack.append(char)
            elif(char == ")" or char== "}",char== "]"):
                if(len(stack)==0):
                    return False
                elif(stack[-1]==pairs[char]):
                    stack.pop()
                else:
                    return False
        if(len(stack)==0):
            return True
        else:
            return False
            
        
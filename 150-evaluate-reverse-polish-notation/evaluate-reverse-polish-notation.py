class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for char in tokens:
            if(char not in "+/*-"):
                stack.append(char)
            else:
                first=int(stack.pop())
                second=int(stack.pop())
                if(char == "+"):
                    result=second+first
                    stack.append(result)
                elif(char == "-"):
                    result=second-first
                    stack.append(result)
                elif(char == "*"):
                    result=second*first
                    stack.append(result)
                else:
                    result=int(second/first)
                    stack.append(result)
        return int(stack[-1])

        
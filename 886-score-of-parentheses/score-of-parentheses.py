class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        score=0
        for i in s:
            if(i=="("):
                stack.append(i)
            if(i==")"):
                stack.pop()
                if(prev=="("):
                    if(len(stack)==0):
                        score+=1
                    else:
                        score+=2 ** len(stack)
            prev=i
        return score


        
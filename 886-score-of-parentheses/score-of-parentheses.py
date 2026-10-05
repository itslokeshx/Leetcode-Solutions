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
                    score+=2 ** len(stack)
            prev=i
        return score


        
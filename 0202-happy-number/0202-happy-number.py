class Solution:
    def isHappy(self, n: int) -> bool:
        num=set()
        flag=True
        while n>0:
            cal=0
            x=0
            while n>0:
                x=n%10
                cal+=x**2
                n=n//10
            n = cal
            if(cal in num):
                n=0
                flag=False
            elif(cal==1):
                flag=True
                break
            else:
                num.add(cal)
                
        return flag
        

        
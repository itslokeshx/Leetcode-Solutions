class Solution:
    def partition(self, s: str) -> list[list[str]]:

        ans=[]
        path=[]

        def backtrack(index):
            if(index == len(s)):
                ans.append(path[:])
                return
            for i in range(index,len(s)):
                pal=s[index:i+1]
                if(pal == pal[::-1]):
                    path.append(pal)
                    backtrack(i+1)
                    path.pop()
        backtrack(0)
        return ans
            


        
        
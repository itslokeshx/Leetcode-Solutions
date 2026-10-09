class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans=[]
        path=[]
        count=0


        def backtrack(index):
            nonlocal count
            for i in range(index,len(candidates)):
                path.append(candidates[i])
                count+=candidates[i]
                if(count == target):
                    ans.append(path[:])
                elif(count < target):
                    backtrack(i)
                count-=candidates[i]   
                path.pop()
        backtrack(0)
        return ans




        
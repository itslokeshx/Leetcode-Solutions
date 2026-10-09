class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        ans=[]
        path=[]
        count=0

        def backtrack(index):
            nonlocal count
            for i in range(index,len(candidates)):
                if(i>index and candidates[i] == candidates[i-1]):
                    continue
                count+=candidates[i]
                path.append(candidates[i])
                if(count == target):
                    ans.append(path[:])
                elif(count < target):
                    backtrack(i+1)
                count-=candidates[i]
                path.pop()
        backtrack(0)
        return ans
        
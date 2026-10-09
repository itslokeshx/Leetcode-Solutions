class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        path=[]
        used=set()

        def backtrack(index):
            nonlocal used
            if(len(path) == len(nums)):
                ans.append(path[:])
                return
            for i in range(0,len(nums)):
                if(nums[i] not in used):
                    path.append(nums[i])
                    used.add(nums[i])
                    backtrack(i)
                    used.remove(nums[i])
                    path.pop()
        backtrack(0)
        return ans
        
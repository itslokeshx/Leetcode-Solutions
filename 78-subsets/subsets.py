class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        ans=[]
        path=[]

        def backtrack(index):

            if(index == len(nums)):
                ans.append(path[:])
                return

            path.append(nums[index])
            backtrack(index+1)
            path.pop()

            backtrack(index+1)

        backtrack(0)

        return ans
            

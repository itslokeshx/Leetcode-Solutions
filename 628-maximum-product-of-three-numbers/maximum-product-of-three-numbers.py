class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()

        firstthree=nums[0] * nums[1] * nums[-1]
        lastthree= nums[-1] * nums[-2] * nums[-3]

        return max(firstthree, lastthree)




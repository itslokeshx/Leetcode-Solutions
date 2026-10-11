class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        given=sum(nums)
        total=(len(nums) * (len(nums) + 1)) // 2
        missing=total-given
        return missing

        
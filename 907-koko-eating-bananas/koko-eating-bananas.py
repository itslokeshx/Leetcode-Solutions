class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while low<=high:
            hours=0
            k=(low+high)//2
            for pile in piles:
                hours+=(pile+k-1)//k
            if(hours > h):
                low=k+1
            else:
                high=k-1
        return low

        
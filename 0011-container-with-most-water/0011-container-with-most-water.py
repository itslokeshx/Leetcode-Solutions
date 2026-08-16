class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        bestarea=0
        area=0
        width=0
        length=0
        while left<right:
            length=min(height[left],height[right])
            width=right-left
            area=length*width
            if(area>bestarea):
                bestarea=area
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1          
        return bestarea
            

        
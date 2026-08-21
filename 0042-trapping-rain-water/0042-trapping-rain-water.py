class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxright=len(height)-1
        maxleft=0
        totalcap=0
        while left < right:
            if(height[left] < height[right]):
                if(height[left] > height[maxleft]):
                    maxleft=left
                if(height[right] > height[maxright]):
                    maxright=right
                totalcap+=(min(height[maxright],height[maxleft])- height[left])
                left+=1
            else:
                if(height[left] > height[maxleft]):
                    maxleft=left
                if(height[right] > height[maxright]):
                    maxright=right
                totalcap+=(min(height[maxright],height[maxleft])- height[right])
                right-=1
        return totalcap




        
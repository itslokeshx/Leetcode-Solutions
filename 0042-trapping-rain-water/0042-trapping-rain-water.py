class Solution:
    def trap(self, height: List[int]) -> int:
        currentleft=0
        currentright=len(height)-1
        maxright=len(height)-1
        maxleft=0
        totalcap=0
        while currentleft < currentright:
            if(height[currentleft] < height[currentright]):
                if(height[currentleft] > height[maxleft]):
                    maxleft=currentleft
                if(height[currentright] > height[maxright]):
                    maxright=currentright
                totalcap+=(min(height[maxright],height[maxleft])- height[currentleft])
                currentleft+=1
            else:
                if(height[currentleft] > height[maxleft]):
                    maxleft=currentleft
                if(height[currentright] > height[maxright]):
                    maxright=currentright
                totalcap+=(min(height[maxright],height[maxleft])- height[currentright])
                currentright-=1
        return totalcap




        
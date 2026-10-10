class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count=0
        if(n==0):
            return True
        if(len(flowerbed) == 1 and flowerbed[0] == 0):
            return True
        for i in range(len(flowerbed)):
            if(
                (flowerbed[i] == 0 )
                and
                (i==len(flowerbed)-1 or flowerbed[i+1]==0) 
                 and
                (flowerbed[i-1]==0 or i==0)
                ):
                count+=1
                flowerbed[i]=1
           
        if(count >= n):
            return True
        else:
            return False
     
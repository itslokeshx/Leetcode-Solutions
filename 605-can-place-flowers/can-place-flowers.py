class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count=0
        for i in range(len(flowerbed)):
            if(len(flowerbed) == 1 and flowerbed[0] == 0):
                count+=1
            elif(flowerbed[i] == 0 and i == 0  and  i< len(flowerbed) and flowerbed[i+1]==0):
                count+=1
                flowerbed[i]=1
            elif(flowerbed[i] == 0 and flowerbed[i-1] == 0 and i==len(flowerbed)-1  ):
                count+=1
                flowerbed[i]=1
            elif(flowerbed[i] == 0 and i>0 and flowerbed[i-1] == 0  and flowerbed[i+1]==0):
                count+=1
                flowerbed[i]=1
        if(count >= n):
            return True
        else:
            return False
     
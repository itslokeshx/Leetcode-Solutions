class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        count=0

        if(n==0):
            return True

        if(len(flowerbed) == 1 and flowerbed[0] == 0):
            return True

        for i in range(len(flowerbed)):
            left_bound =  i==0 or flowerbed[i-1]==0 
            right_bound = i==len(flowerbed)-1 or flowerbed[i+1]==0
            if(flowerbed[i] == 0 and right_bound and left_bound):
                count+=1
                flowerbed[i]=1

        if(count >= n):
            return True
        else:
            return False
     
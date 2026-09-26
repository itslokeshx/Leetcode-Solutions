class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        finalrow=[0]*numRows
        finalrow[0]=[1]
        for i in range(1,numRows):
            prerow=finalrow[i-1]
            currrow=[1]*(i+1)
            for j in range(1,i):
                currrow[j]=prerow[j-1]+prerow[j]
            finalrow[i]=currrow
        return finalrow
        
                
            

        
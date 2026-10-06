class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue=deque()
        minutes=-1
        fresh=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 2):
                    queue.append((i,j))
                elif(grid[i][j]==1):
                    fresh+=1
        if(fresh==0):
            return 0
        while queue:
            for i in range(len(queue)):
                r,c=queue.popleft()
                if(r>0 and grid[r-1][c] == 1):
                    grid[r-1][c]=2
                    fresh-=1
                    queue.append((r-1,c))
                if(c>0 and grid[r][c-1] == 1):
                    grid[r][c-1]=2
                    fresh-=1
                    queue.append((r,c-1))
                if(r < len(grid)-1 and grid[r+1][c] == 1):
                    grid[r+1][c]=2
                    fresh-=1
                    queue.append((r+1,c))
                if(c < len(grid[0])-1 and grid[r][c+1] == 1):
                    grid[r][c+1]=2
                    fresh-=1
                    queue.append((r,c+1))
            minutes+=1

        if(fresh > 0):
            return -1
        else:
            return minutes

                
        
    
        
                


        
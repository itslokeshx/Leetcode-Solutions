class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:

        visited=set()
        op=[]
        pac=False
        atl=False

        def dfs(r,c):

            nonlocal pac
            nonlocal atl

            visited.add((r,c))

            if(r>0 and heights[r-1][c] <= heights[r][c]):
                if( (r-1,c) not in visited):
                    dfs(r-1,c)
            if(r+1 < len(heights) and heights[r+1][c] <= heights[r][c]):
                if( (r+1,c) not in visited):
                    dfs(r+1,c)
            if(c>0 and heights[r][c-1] <= heights[r][c]):
                if( (r,c-1) not in visited):
                    dfs(r,c-1)
            if(c+1 < len(heights[0]) and heights[r][c+1] <= heights[r][c]):
                if( (r,c+1) not in visited):
                    dfs(r,c+1)

            if(r==0 or c==0):
                pac=True
            if(r==len(heights)-1 or c==len(heights[0])-1):
                atl=True


        for i in range(0,len(heights)):
            for j in range(0,len(heights[0])):
                    visited=set()
                    pac=False
                    atl=False
                    dfs(i,j)
                    if(pac and atl):
                        op.append([i,j])
        return op

        
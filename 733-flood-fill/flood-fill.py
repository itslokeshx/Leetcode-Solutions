class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

        original=image[sr][sc]

        stack=[]

        def dfs(r,c):

            stack.append([r,c])

            if( r > 0 and image[r-1][c] == original):
                if([r-1,c] not in stack):
                    dfs(r-1,c)
                
            if( r+1 <len(image) and image[r+1][c] == original):
                if([r+1,c] not in stack):
                    dfs(r+1,c)

            if( c > 0 and image[r][c-1] == original):
                if([r,c-1] not in stack):                
                    dfs(r,c-1)

            if( c+1 < len(image[0]) and image[r][c+1] == original):
                if([r,c+1] not in stack):
                    dfs(r,c+1)
            image[r][c]=color
        dfs(sr,sc)
        return image
            



        
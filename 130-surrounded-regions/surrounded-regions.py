class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited=set()
        region=True

        def dfs(r,c):
            nonlocal region

            visited.add((r,c))
            regioncells.append((r,c))

            if(r > 0 and board[r - 1][c] == "O"):
                if (r - 1, c) not in visited:
                    dfs(r - 1, c)

            if(r + 1 < len(board) and board[r + 1][c]  == "O"):
                if (r + 1, c) not in visited:
                    dfs(r + 1, c)

            if(c > 0 and board[r][c - 1] == "O"):
                if (r,c-1) not in visited:
                    dfs(r, c - 1)

            if(c + 1 < len(board[0]) and board[r][c + 1] == "O"):
                if (r,c+1) not in visited:
                    dfs(r, c + 1)
            if( r==0 or c==0 or r == len(board) - 1 or c == len(board[0])-1):
                region=False

        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if(board[i][j] == "O" and (i,j) not in visited):
                    region=True
                    regioncells=[]
   
                    dfs(i,j)
                    if(region):
                        for r,c in regioncells:
                            board[r][c]="X"

        
            
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

        original = image[sr][sc]
        if original == color:
            return image

        def dfs(r, c):
            image[r][c] = color
            if r > 0 and image[r-1][c] == original:
                    dfs(r-1, c)
            if r + 1 < len(image) and image[r+1][c] == original:
                    dfs(r+1, c)
            if c > 0 and image[r][c-1] == original:
                    dfs(r, c-1)
            if c + 1 < len(image[0]) and image[r][c+1] == original:
                    dfs(r, c+1)
        dfs(sr, sc)
        return image
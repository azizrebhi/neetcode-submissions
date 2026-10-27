class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
     scolor=image[sr][sc]
     ROWS, COLS = len(image), len(image[0])
     def dfs(r,c,visit):
       if (min(r, c) < 0 or
          r == ROWS or c == COLS or
          (r, c) in visit or image[r][c] !=scolor):
             return 
       if image[r][c]==scolor :
          image[r][c]=color

       visit.add((r, c))

       dfs(r + 1, c, visit)
       dfs(r - 1, c, visit)
       dfs(r, c + 1, visit)
       dfs(r, c - 1, visit)

       visit.remove((r, c))
     dfs(sr,sc,set())
     return image

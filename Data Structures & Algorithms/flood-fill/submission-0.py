class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
      colorc=image[sr][sc]
      if colorc==color:
        return image
      def Fill(sr, sc) :
         ROW ,COL=len(image),len(image[0])
         if min(sr,sc)<0 or sr==ROW or sc==COL :
            return 
         if image[sr][sc]!=colorc:
            return
         image[sr][sc]=color
         Fill(sr-1,sc)
         Fill(sr+1,sc)
         Fill(sr, sc-1)
         Fill( sr,sc+1)

      Fill(sr,sc) 
      return image
        
      

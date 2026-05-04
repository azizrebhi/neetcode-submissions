class Solution:

    def encode(self, strs: List[str]) -> str:
        encode=""
        for c in strs :   
          encode+=str(len(c))+"#"+c
        return encode 
    def decode(self, s: str) -> List[str]:
       res,i=[],0
       while i<len(s):
         j=i
         while s[j] != "#":
            j+=1 
         res.append(s[j+1:j+1+int(s[i:j])])
         i=j+int(s[i:j])+1
       return res
             
   
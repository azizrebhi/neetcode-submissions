class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m={}
        for c in s :
           m[c]=m.get(c,0)+1
        k={}
        for b in t : 
          k[b]=k.get(b,0)+1
        return k==m
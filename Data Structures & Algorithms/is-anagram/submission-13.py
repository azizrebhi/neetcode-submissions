class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m=[0]*26
        for c in s :
           m[ord(c)-ord("a")]+=1
        for b in t : 
          m[ord(b)-ord("a")]-=1
        return m==[0]*26
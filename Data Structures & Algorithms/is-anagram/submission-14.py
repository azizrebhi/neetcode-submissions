class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        m=[0]*26
        for i in range(len(s)) :
           m[ord(s[i])-ord("a")]+=1 
           m[ord(t[i])-ord("a")]-=1
        return m==[0]*26
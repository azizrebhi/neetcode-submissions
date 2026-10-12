class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L=0
        R=len(s1)-1
        s1=sorted(s1)
        while R<len(s2):
            if sorted(s2[L:R+1])==s1:
                return True
            L+=1
            R+=1
        return False
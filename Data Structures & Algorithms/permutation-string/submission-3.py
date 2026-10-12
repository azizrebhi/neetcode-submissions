class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L=0
        count={}
        for i in s1 : 
            count[i]=1+count.get(i,0)
        count1={}
        for R in range(len(s2)):
            count1[s2[R]]=1+count1.get(s2[R],0)
            if R-L+1==len(s1):
                if count==count1:
                    return True
                count1[s2[L]]-=1
                if count1[s2[L]]==0 : 
                    del count1[s2[L]]
                L+=1
            
        return False
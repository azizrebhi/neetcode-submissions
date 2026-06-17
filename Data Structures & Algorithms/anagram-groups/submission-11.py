class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indeces = defaultdict(list)
        
        res=[]
        for s in strs:
            L=[0]*26
            for i in s:
                L[ord(i.upper())-65]+=1
            indeces[tuple(L)].append(s)
        for k in indeces :
            res.append(indeces[k])
        return res


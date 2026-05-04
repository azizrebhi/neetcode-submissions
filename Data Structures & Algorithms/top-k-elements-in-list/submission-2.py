class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(0,len(nums)+1)]
        for s in nums :
            count[s]=1+count.get(s,0)
        for c,n in count.items() :
            freq[n].append(c)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

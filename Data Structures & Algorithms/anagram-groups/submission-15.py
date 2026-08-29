class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for char in strs :
            l=[0]*26
            for c in char:
              l[ord(c)-ord("a")]+=1
            t=tuple(l)
            m[t].append(char)
        return list(m.values())

         

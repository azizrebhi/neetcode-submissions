class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        charset=set()
        res=0
        for r in range(len(s)):
            if s[r] in charset :
                res=max(res,len(charset))
                while s[l]!=s[r]:
                    charset.discard(s[l])
                    l+=1
                charset.discard(s[l])
                l += 1

            charset.add(s[r])
        return max(res,len(charset)) 

            
        
        
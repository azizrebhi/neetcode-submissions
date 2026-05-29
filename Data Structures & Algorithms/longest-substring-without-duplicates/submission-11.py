class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L=0
        window={}
        length=float("-inf")
        if s=="":
            return 0
        for R in range(len(s)):
            if s[R] in window and window[s[R]] >= L :
                L=window[s[R]]+1
            window[s[R]]=R
            length = max(length, R - L + 1)
        return length

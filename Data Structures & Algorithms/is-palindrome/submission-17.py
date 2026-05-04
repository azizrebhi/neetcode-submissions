class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = re.sub(r'[^a-zA-Z0-9]', '', s)
        r,l=0,len(clean_s)-1
        B=True
        while(r<l):
            if(clean_s[r].lower()!=clean_s[l].lower()):
                B=False 
                break
            r=r+1
            l=l-1
        return B 
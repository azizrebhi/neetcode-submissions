class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<=r:
            if s[r].isalnum() and s[l].isalnum():

              if s[r].lower()!=s[l].lower():
                return False
              l+=1
              r-=1
            elif not s[r].isalnum():
              r-=1
            else :
              l+=1
                 
        return True
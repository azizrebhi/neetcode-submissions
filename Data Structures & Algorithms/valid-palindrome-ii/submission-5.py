class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_perfect_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        l,r=0,len(s)-1
        while l<r:
            if not s[r].isalnum():
                r-=1
            elif not s[l].isalnum():
                l+=1
            else :
               if s[r]!=s[l]:
                   return is_perfect_palindrome(l+1,r) or is_perfect_palindrome(l,r-1)
               l+=1
               r-=1
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join(c for c in s if c.isalnum())
        right ,left =0,len(res)-1
        while right<left :
            if res[right].lower()!=res[left].lower():
                return False
            right +=1
            left-=1
        return True
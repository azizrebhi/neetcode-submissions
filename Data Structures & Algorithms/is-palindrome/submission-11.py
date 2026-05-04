class Solution:
    def isPalindrome(self, s: str) -> bool:
         s1 = "".join(c.lower() for c in s if c.isalnum())  # Garder seulement les lettres, en minuscule
         left, right = 0, len(s1) - 1  # ✅ Correction de l'initialisation

         while left < right:  # ✅ `left < right` au lieu de `right <= left`
            if s1[left] != s1[right]:  # ✅ `s1` est déjà en minuscule, pas besoin de `.lower()`
                return False
            left += 1
            right -= 1
            
         return True  # ✅ Correction de `return B`

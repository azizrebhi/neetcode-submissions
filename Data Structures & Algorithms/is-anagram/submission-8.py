class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if len(s)!=len(t):
          return False
       else :
            counts={}
            counts1={}
            for char in s:
                counts[char] = counts.get(char, 0) + 1
            for char in t:
                 counts1[char] = counts1.get(char, 0) + 1
            if counts1==counts :
                return True 
            else : 
                return False 
            
            
        
            
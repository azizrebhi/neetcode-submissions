class Solution:
    def isValid(self, s: str) -> bool:
       closed_to_open={"}":"{","]":"[",")":"("}
       stack=[]
       for i in s :
            if i  in  closed_to_open.values():
                stack.append(i)
            else:
              #closed Parenthese with no previous one open
              if not stack:
                return False
              if closed_to_open[i]!=stack[-1]:
                return False
              stack.pop()
            
            
       return len(stack)==0
              
                

            
        
                 


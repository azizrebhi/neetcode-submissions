class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        m=0
        for i in tokens : 
            if i not in ["+", "-", "*", "/"]:
               stack.append(i)
            else :
               a=int(stack.pop())
               b=int(stack.pop())
               if i=="+":
                  m=b+a
               elif i=="-":
                  m=b-a
               elif i=="*" :
                  m=b*a
               elif i=="/":
                  m=int(b/a)
               stack.append(m)
        
        return int(stack[-1])


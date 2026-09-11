class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for t in tokens : 
            if t.lstrip('-').isdigit():
                s.append(int(t))
            else : 
                a=s.pop()
                b=s.pop()
                if t=="+" :
                    s.append(a+b)
                elif t=="-":
                    s.append(b-a)
                elif t=="*" :
                    s.append(a*b)
                elif t=="/" :
                    s.append(int(b/a))
        
        return s.pop()
    


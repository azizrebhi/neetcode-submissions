class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stack=[]
        res=[]
        for i in parts : 
          if i!="" and i!=".":
            if i != "..":
                stack.append(i)
            else :
              if stack : 
                stack.pop()
        res.append("/".join(stack))
        return "/"+res[0]
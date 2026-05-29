class Solution:
    def calPoints(self, operations: List[str]) -> int:
       stack=[]
       score=0
       for op in operations : 
          if op=="+":
             stack.append(str(int(stack[-1])+int(stack[-2])))
          elif op=="D":
              stack.append(str(int(stack[-1])*2))
          elif op == "C":
              stack.pop()
          else :
             stack.append(op)
             score=op
       sum=0
       for j in stack : 
          sum+=int(j)
       return sum

         
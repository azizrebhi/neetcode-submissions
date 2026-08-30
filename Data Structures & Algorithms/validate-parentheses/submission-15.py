class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        closed_to_open={")":"(","]":"[","}":"{"}
        for c in s :
          if c in closed_to_open : 
            if  len(st)==0 :
              return False
            elif closed_to_open[c]==st[-1]:
              st.pop()
            else : 
              return False
          else :
            st.append(c)
        if len(st)!=0 :
          return False 
        return True 
        

              


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        B=True 
        k=0
        for j in range(len(board)):
          lst=[]
          for sublist in board : 
              sublist1=[item for item in sublist if item.isdigit()]   
              s=set(sublist1) 
              if(len(s)!=len(sublist1)):
                B=False   
              lst.append(sublist[j])
          lst=[item for item in lst if item.isdigit()]
          k=set(lst)
          if(len(k)!=len(lst)):
                B=False
        if (B==True):
            for k in range(0,7,3):
                for c in range(0,7,3):
                    sub=[row[c:c+3] for row in board[k:k+3]]
                    l=sum(sub, [])
                    l=[item for item in l if item.isdigit()]
                    x=set(l)
                    if len(x)!=len(l):
                        B=False
        else : return B 
        return B        










        
                 
                    
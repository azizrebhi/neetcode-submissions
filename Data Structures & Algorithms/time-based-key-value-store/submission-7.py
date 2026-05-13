class TimeMap:

    def __init__(self):
        self.store={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
           self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
          left,right=0,len(self.store[key])-1
          res=""
          while left<=right:
            m=(left+right)//2
            if self.store[key][m][0]>timestamp:
                right=m-1
            elif self.store[key][m][0]<timestamp:
                res=self.store[key][m][1]
                left=m+1
            else : 
                return self.store[key][m][1]
            
          return res
        else : 
            return ""     


        

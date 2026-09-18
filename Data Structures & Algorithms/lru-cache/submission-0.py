class Node : 
    def __init__(self,key,val=0):
        self.key,self.val=key,val
        self.prev=self.next=None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.right,self.left=Node(0),Node(0)
        self.right.prev=self.left
        self.left.next=self.right
    def remove (self,node):
        prev,nxt=node.prev,node.next
        prev.next,nxt.prev=nxt,prev
    #insert always to the right to mark it as recently used
    def insert (self,node):
        prev=self.right.prev
        prev.next=node
        self.right.prev=node
        node.next=self.right
        node.prev=prev

    
    def get(self, key: int) -> int:
       if key in self.cache : 
          self.remove(self.cache[key])
          self.insert(self.cache[key])
          return self.cache[key].val
       return -1
           

    def put(self, key: int, value: int) -> None:
        if key in self.cache : 
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.capacity :
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]


            

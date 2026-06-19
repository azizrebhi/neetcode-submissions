"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        OldToCopy={}
        while curr : 
            copy=Node(curr.val)
            OldToCopy[curr]=copy
            curr=curr.next
        for temp in OldToCopy :
            if temp.random :
             OldToCopy[temp].random=OldToCopy[temp.random]
            else : 
                OldToCopy[temp].random=None
            if temp.next :
             OldToCopy[temp].next=OldToCopy[temp.next]
            else : 
                OldToCopy[temp].next=None
        return OldToCopy[head] if head else None

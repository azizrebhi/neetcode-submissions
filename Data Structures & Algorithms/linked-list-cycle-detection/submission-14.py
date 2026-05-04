# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast , slow = head.next,head
        if head.next==None :
            return False
        else:
         while fast.next and fast!=slow  : 
            slow=slow.next
            fast=fast.next.next
           
         if fast.next :
            return True 
         else :
            return False
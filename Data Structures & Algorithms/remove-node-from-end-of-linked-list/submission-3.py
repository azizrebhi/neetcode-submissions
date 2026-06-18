# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        s=0
        while curr:
           curr=curr.next
           s+=1
        n=s-n
        if n==0:
            return head.next
        prev,curr=None ,head
        while n>0:
            prev=curr
            curr=curr.next
            n-=1
        
        prev.next=curr.next
        return head
        



       
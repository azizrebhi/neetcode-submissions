# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        if not head.next:
            return None
        size=0
        curr=head
        while curr : 
            curr=curr.next
            size+=1
        m=size-n
        curr=head
        i=0
        while i<m-1:
            curr=curr.next
            i=i+1
        if m ==0:
            return head.next
        curr.next=curr.next.next
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow =fast=head
        while fast and fast.next : 
          fast=fast.next.next
          slow=slow.next
        mid=slow.next
        slow.next=None
        prev=None
        curr=mid
        while curr :
            temp=curr
            curr=curr.next
            temp.next=prev
            prev=temp    
        curr = head
        while prev: 
            # Save the next targets for both pointers before modifying links
            next_curr = curr.next
            next_prev = prev.next
            
            # Rewire the connections
            curr.next = prev
            prev.next = next_curr
            
            # Step forward using the saved targets
            curr = next_curr
            prev = next_prev

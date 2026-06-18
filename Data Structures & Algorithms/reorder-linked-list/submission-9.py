# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev=None
        curr=slow
        while curr : 
            temp=curr
            curr=curr.next
            temp.next=prev
            prev=temp
        dummy=ListNode()
        while head!=slow  : 
            dummy.next=head
            dummy=dummy.next
            head=head.next
            dummy.next=prev
            dummy=dummy.next
            prev=prev.next
            

            


        

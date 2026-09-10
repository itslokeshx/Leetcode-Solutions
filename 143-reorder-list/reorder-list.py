# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None
        prev=None
        curr=mid
        while curr is not None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        second=prev
        dummy=ListNode(0)
        dummy.next=head
        final=dummy.next
        while second is not None:
            first_next=final.next
            second_next=second.next
            final.next=second
            second.next=first_next
            final=first_next
            second=second_next
        return final







    

    




     
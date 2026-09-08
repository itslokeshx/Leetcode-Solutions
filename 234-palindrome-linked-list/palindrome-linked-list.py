# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        

        slow=head
        fast=head
        flag=False

        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        mid=slow
        prev=None
        curr=mid

        while curr is not None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        while prev is not None:
            if(head.val == prev.val):
                head=head.next
                prev=prev.next
                flag= True
            else:
                flag=False
                break
        return flag
        
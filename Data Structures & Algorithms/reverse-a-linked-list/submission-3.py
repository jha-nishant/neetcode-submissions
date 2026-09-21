# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListIterative(head)
        # return self.reverseListRecursive(head)
    
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        rev = None
        current = head
        while current:
            next = current.next
            current.next = rev
            rev = current
            current = next
        return rev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        next = head.next
        rev = self.reverseList(next)
        next.next = head
        head.next = None
        return rev

        
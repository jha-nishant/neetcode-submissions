import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return 
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        
        half = math.ceil(length / 2)

        count = 0
        current = head
        prev = None
        while count < half:
            count += 1
            prev = current
            current = current.next
        prev.next = None
        second = self.reverseList(current)

        p1 = head
        p2 = second
        current = None
        while p1 and p2:
            p1_next = p1.next
            p2_next = p2.next
            if current:
                current.next = p1
            p1.next = p2
            p2.next = None
            current = p2
            p1 = p1_next
            p2 = p2_next
        
        if p1:
            current.next = p1

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        next = head.next
        rev = self.reverseList(next)
        next.next = head
        head.next = None
        return rev




        
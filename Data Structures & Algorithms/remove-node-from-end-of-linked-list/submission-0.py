# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        first = dummy
        second = dummy

        count = 0
        while count < n:
            count += 1
            first = first.next

        while first.next:
            first = first.next
            second = second.next

        next = second.next
        second.next = next.next

        return dummy.next

        
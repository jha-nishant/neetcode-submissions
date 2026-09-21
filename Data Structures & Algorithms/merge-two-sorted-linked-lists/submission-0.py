# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        dummy = ListNode(-1)
        current = dummy
        while list1 and list2:
            value1, value2 = list1.val, list2.val
            if value1 < value2:
                next = list1.next
                current.next = list1
                current = list1
                list1 = next

            else:
                next = list2.next
                current.next = list2
                current = list2
                list2 = next
        
        if list1:
            current.next = list1
        
        if list2:
            current.next = list2
        
        return dummy.next
